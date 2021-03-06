<%@ page pageEncoding="utf-8" %>
<%@ include file="/views/guide/xf/three/middle/guide_add_friends.jsp"%>	
<div id="replyDiv" class="reply-notify news-feed" style="display:none"><%-- 异步加载 --%>
	<div class="section-header">
		<h2>新留言及回复<span class="stat"><a id="gossipReplyCount" href="${applicationScope.urlWww}/myreplylist.do"></a></span></h2>
		<span class="more" id="replyMoreDiv"><a href="${applicationScope.urlWww}/myreplylist.do">更多</a></span>
	</div>
	<div id="opilist" class="feed-story"></div>
</div>	
<%@ include file="/views/guide/xf/three/middle/guide_xf_newsfeed.jsp"%>	
<div class="find-friend-box">		
	<div class="find-friend-body">
		<div class="feed-arrow"></div>
		<h4>添加好友以获取好友新鲜事</h4>	
		<%@ include file="/views/guide/xf/common/middle/guide_middle_search.jsp"%>	
		<c:if test="${!empty requestScope.companyAndSchool}">	
			<c:forEach varStatus="status" var="csItem" items="${requestScope.companyAndSchool}">
				<c:if test="${csItem.count>0}">				
					<div class="users">
				       	<h4>
				       		<c:choose>	
				       			<c:when test="${csItem.type=='location'}">
				       				${csItem.typeName}
				       			</c:when>
				       			<c:when test="${csItem.type=='work'}">
				       				<a href=${applicationScope.urlBrowse}/searchEx.do?ref=sg_guide_${csItem.type}_search&amp;${csItem.moreLink} target="_blank">${csItem.typeName}</a> 
				       				的同事<span class="num">${csItem.count}人</span>
				       			</c:when>
				       			<c:otherwise>
									<a href=${applicationScope.urlBrowse}/searchEx.do?ref=sg_guide_${csItem.type}_search&amp;${csItem.moreLink} target="_blank">${csItem.typeName}</a> 
				       				的同学<span class="num">${csItem.count}人</span>	
								</c:otherwise>
							</c:choose>	
				       	</h4>
						<ul class="clearfix" id="guids-uses-con${status.index}"></ul>
				    </div>
				    <c:if test="${csItem.type!='location'}">
						<div id="showLessCon${status.index}" class="show-more">
							<a href=${applicationScope.urlBrowse}/searchEx.do?ref=sg_guide_${csItem.type}_search&amp;${csItem.moreLink} target="_blank">
								显示更多&raquo;
							</a>
						</div>
					</c:if>					
				</c:if>			
			</c:forEach>	
		</c:if>	
		<c:if test="${fn:length(sameIPList)>0}">				
			<div class="users">
		       	<h4>在你附近上网</h4>
				<ul class="clearfix" id="guids-uses-con99"></ul>
		    </div>
			<div id="showLessCon99" class="show-more" style="display:none"></div>		
		</c:if>	
	</div>
</div>
<c:if test="${requestScope.guide_social=='social_bad'}">
	<%@ include file="/views/guide/xf/common/middle/guide_hot_share.jsp"%>
</c:if>
                            	
