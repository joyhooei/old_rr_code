package com.renren.xoa.registry;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Map.Entry;
import java.util.concurrent.ConcurrentHashMap;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

/**
 * XoaRegistry的一个基础实现类
 * 
 * @author Li Weibo (weibo.leo@gmail.com) //I believe spring-brother
 */
public abstract class AbstractXoaRegistry implements XoaRegistry {

    protected Log logger = LogFactory.getLog(this.getClass());

    /**
     * 监听器
     */
    @SuppressWarnings("unchecked")
    protected List<XoaRegistryListener> listeners = Collections.EMPTY_LIST;
    
	/**
	 * 容器map
	 */
	private Map<String, Wrapper> map = new ConcurrentHashMap<String, Wrapper>();

    private Map<String, List<XoaServiceDescriptor>> serviceNodesMap = new ConcurrentHashMap<String, List<XoaServiceDescriptor>>();

	/* (non-Javadoc)
	 * @see com.renren.xoa.registry.XoaRegistry#queryService(java.lang.String)
	 */
	public XoaServiceDescriptor queryService(String serviceId) {
		
		Wrapper wrapper = getWrapper(serviceId);
		if (wrapper == null) {
			return null;
		}
		return wrapper.get();
	}
	
	/**
	 * 根据指定的serviceId获取一个Wrapper
	 * @param serviceId
	 * @return
	 */
	protected Wrapper getWrapper(String serviceId) {
		Wrapper wrapper = map.get(serviceId);
		if (wrapper == null) {
			synchronized (serviceId.intern()) {
				wrapper = map.get(serviceId);
				if (wrapper == null) {
					List<XoaServiceDescriptor> nodes = getServiceNodes0(serviceId);
					if (nodes == null || nodes.size() == 0) {
						return null;
					}
					
					//排序
					Collections.sort(nodes, XoaServiceDescriptor.COMPARATOR);
					
					//提取enabledNodes
					List<XoaServiceDescriptor> enabledNodes = new ArrayList<XoaServiceDescriptor>();
					for (XoaServiceDescriptor node : nodes) {
					    if (!node.isDisabled()) {
					        enabledNodes.add(node);
					    }
					}
					
					if(logger.isInfoEnabled()) {
					    StringBuilder sb = new StringBuilder();
					    sb.append("Got ");
					    sb.append(enabledNodes.size());
					    sb.append(" enabled nodes in xoa-registry: ");
					    for (XoaServiceDescriptor node : enabledNodes) {
					        sb.append(node);
					        sb.append(",");
					    }
					    
					    //remove trailing ','
					    if (sb.charAt(sb.length() - 1) == ',') {
					        sb.setLength(sb.length() - 1);
					    }
					    logger.info(sb);
					}
					
					wrapper = new Wrapper(enabledNodes);
					map.put(serviceId, wrapper);
					
					storeServiceNodes(serviceId, nodes);
				}
			}
		}
		return wrapper;
	}
	
	@Override
	public List<XoaServiceDescriptor> queryServices(String serviceId) {
		Wrapper wrapper = getWrapper(serviceId);
		if (wrapper == null) {
			return null;
		}
		return wrapper.getAll();
	}
	
	private List<XoaServiceDescriptor> getServiceNodes0(String serviceId) {
		
		//在System property中配置XOA服务节点的hostport，可以覆盖掉registry中的配置。
		//格式为：host1:port1,host2:port2
		String hosts = getHostConfigFromSysProp(serviceId);
		if (hosts != null) {
			List<XoaServiceDescriptor> descs = new ArrayList<XoaServiceDescriptor>();
			String hostss[] = hosts.split(",");
			for (String host : hostss) {
				String[] ss = host.split(":");
				if (ss.length == 2) {
					
					XoaServiceDescriptorBase desc = new XoaServiceDescriptorBase();
					desc.setServiceId(serviceId);
					desc.setIpAddress(ss[0]);
					desc.setPort(Integer.parseInt(ss[1]));
					descs.add(desc);
				}
			}
			if (descs.size() > 0) {
				logger.warn("Using system property to locate XOA service nodes:" + hosts);
				return descs;
			}
		}
		return getServiceNodes(serviceId);
	}
	
	private String getHostConfigFromSysProp(String serviceId) {
		return System.getProperty(getHostsPropertyName(serviceId));
	}
	
	/**
	 * 在System property中配置XOA服务节点的hostport，可以覆盖掉registry中的配置。
	 * 
	 * 通过这个方法来获取System property的名字
	 * 
	 * @param serviceId
	 * @return
	 */
	private String getHostsPropertyName(String serviceId) {
		return "xoa.hosts." + serviceId;
	}
	
	/**
	 * 根据指定的serviceId获取服务节点
	 * @param serviceId
	 * @return
	 */
	public abstract List<XoaServiceDescriptor> getServiceNodes(String serviceId);
	
	/**
	 * 更新指定serviceId的服务节点
	 * @param serviceId
	 * @param nodes
	 */
    protected void updateServiceNodes(String serviceId, List<XoaServiceDescriptor> nodes) {
		if (nodes == null || nodes.size() == 0) { //传入不能为空
			logger.error("node list empty to update for service:" + serviceId);
			return;
		}
		if (getHostConfigFromSysProp(serviceId) != null) {    //如果配置了system property，就还按其配置来
			if (logger.isInfoEnabled()) {
				logger.info("Still using system property conf for hosts: "
						+ getHostConfigFromSysProp(serviceId));
			}
		} else {
		    
		    //先排序
		    Collections.sort(nodes, XoaServiceDescriptor.COMPARATOR);
		    
			boolean hasDisabledNode = false; //记录是否有节点被disable了
			List<XoaServiceDescriptor> enabledNodes = new ArrayList<XoaServiceDescriptor>(nodes.size());
			for (XoaServiceDescriptor node : nodes) {
				if (!node.isDisabled()) {
					enabledNodes.add(node);
				} else {
					hasDisabledNode = true;
					/*if (logger.isInfoEnabled()) {
						logger.info("Node disabled for service "
								+ node.getServiceId() + ": "
								+ node.getIpAddress() + ":" + node.getPort());
					}*/
				}
			}
			
			List<XoaServiceDescriptor> serviceNodes = serviceNodesMap.get(serviceId);
			
			//寻找被disable掉的节点，并触发相应事件
			if (hasDisabledNode) {
                for (XoaServiceDescriptor node : nodes) {   //遍历寻找所有的disabled node
                    if (node.isDisabled()) {
                        fireNodeDisabled(node); //触发onNodeDisabled事件
                    }
                }
            }
			
			if (serviceNodes != null) {
			  //寻找被删除掉的节点，并触发相应事件
	            for(XoaServiceDescriptor thisNode : serviceNodes) {
	                boolean found = false;
	                for (XoaServiceDescriptor node : nodes) {
	                    
	                    //只比较IP和端口
	                    if (node.getIpAddress().equals(thisNode.getIpAddress())
	                        && node.getPort() == thisNode.getPort()) {
	                        found = true;
	                        break;
	                    }
	                }
	                if (!found) {
	                    fireNodeDeleted(thisNode);
	                }
	            }
			}
			
			if (logger.isInfoEnabled()) {    //log出这次更新的细节
				
				StringBuilder sb = new StringBuilder();
				sb.append(serviceId);
				sb.append(" updated, now ");
				sb.append(enabledNodes.size());
				sb.append(" nodes: ");
				for (XoaServiceDescriptor node : enabledNodes) {
					sb.append(node.getIpAddress());
					sb.append(":");
					sb.append(node.getPort());
					sb.append(",");
				}
				if (sb.charAt(sb.length() - 1) == ',') {
					sb.setLength(sb.length() - 1);	//remove tailing ','
				}
				if (hasDisabledNode) {	//存在disabled nodes就打印这段log
					sb.append("; disabled nodes: ");
					for (XoaServiceDescriptor node : nodes) {
						if (node.isDisabled()) {
							sb.append(node.getIpAddress());
							sb.append(":");
							sb.append(node.getPort());
							sb.append(",");
						}
						
					}
					if (sb.charAt(sb.length() - 1) == ',') {
						sb.setLength(sb.length() - 1);	//remove tailing ','
					}
				}
				logger.info(sb.toString());
			}
			
			//把当前所有enabled的节点注册进去
			map.put(serviceId, new Wrapper(enabledNodes));
			storeServiceNodes(serviceId, nodes);
		}
	}
	
    /**
     * 把当前registry中配置的那些节点保存起来，以便后续检测变更情况
     * 
     * @param nodes
     */
    private void storeServiceNodes(String serviceId, List<XoaServiceDescriptor> nodes) {
        //把传入的nodes列表copy一遍，方式上层的修改
        List<XoaServiceDescriptor> copy = new ArrayList<XoaServiceDescriptor>(nodes.size());
        for (XoaServiceDescriptor node : nodes) {
            copy.add(node);
        }

        //包装成不可修改了，赋值给成员变量
        this.serviceNodesMap.put(serviceId, Collections.unmodifiableList(copy));
    }
    
    /**
     * 触发所有listener的onNodeDeleted事件
     * @param node
     */
	private void fireNodeDeleted(XoaServiceDescriptor node) {
	    for(XoaRegistryListener l : listeners) {
            l.onNodeDeleted(node);
        }
    }

    /**
     * 触发所有listener的onNodeDisabled事件
     * @param node
     */
    private void fireNodeDisabled(XoaServiceDescriptor node) {
	    for(XoaRegistryListener l : listeners) {
	        l.onNodeDisabled(node);
	    }
    }

    /**
	 * @return 所有注册的serviceId
	 */
	protected Set<String> getServiceIds() {
		return map.keySet();
	}
	
	/**
	 * 服务器配置列表的一个封装，同时提供简单的轮询负载均衡
	 */
	public static class Wrapper {
		
		private XoaServiceDescriptor[] descriptors;
		
		/**
		 * 轮询访问时用到的index
		 */
		private int index = 0;
		
		public Wrapper(List<XoaServiceDescriptor> descriptorList) {
			descriptors = new XoaServiceDescriptor[descriptorList.size()];
			int offset = 0;
			for (XoaServiceDescriptor d : descriptorList) {
				descriptors[offset++] = d;
			}
		}
		
		/**
		 * 获取一个 XoaServiceDescriptor，使用简单的轮询负载均衡
		 * @return
		 */
		public XoaServiceDescriptor get() {
			
			if (index > Integer.MAX_VALUE - 10000) {	//reset
				index = 0;
			}
			return descriptors[index++ % descriptors.length];
		}
		
		/**
		 * @return 返回所有服务节点的描述符
		 */
		public List<XoaServiceDescriptor> getAll() {
			List<XoaServiceDescriptor> ret = new ArrayList<XoaServiceDescriptor>(descriptors.length);
			for (XoaServiceDescriptor desc : descriptors) {
				ret.add(desc);
			}
			return ret;
		}
	}
	
    @Override
    public List<String> lookup(String ip, int port) {
        List<String> serviceIds = new ArrayList<String>();
        for (Entry<String, List<XoaServiceDescriptor>> entry : serviceNodesMap.entrySet()) {
            for (XoaServiceDescriptor node : entry.getValue()) {
                if (node.getIpAddress().equals(ip) && 
                        node.getPort() == port && !node.isDisabled()) {
                    serviceIds.add(entry.getKey());
                }
            }
        }
        Collections.sort(serviceIds);
        return serviceIds;
    }

    @Override
    public void addListener(XoaRegistryListener listener) {
        if (listeners == Collections.EMPTY_LIST) {
            listeners = new ArrayList<XoaRegistryListener>();
        }
        this.listeners.add(listener);
    }
    
    @Override
    public XoaService getService(String serviceId) {
        throw new UnsupportedOperationException();
    }
    
    @Override
    public List<XoaService> getServices() {
        throw new UnsupportedOperationException();
    }
}
