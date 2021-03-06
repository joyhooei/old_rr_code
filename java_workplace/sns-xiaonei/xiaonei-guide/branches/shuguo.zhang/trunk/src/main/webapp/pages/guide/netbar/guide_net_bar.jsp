<%@ page contentType="text/html;charset=UTF-8" session="false"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://struts.apache.org/tags-html" prefix="html"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<%@ taglib uri="http://jakarta.apache.org/taglibs/string-1.1" prefix="str" %>
<%@ taglib uri="http://www.renren.com/tags-core" prefix="xn" %>
<%@ page import="com.xiaonei.platform.component.tools.UserUtil" %>
<%
com.xiaonei.platform.core.model.User user = null;
%>
<%
try {
	user = (com.xiaonei.platform.core.model.User)request.getAttribute("host");	
} catch(Exception e) {
}
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<c:set var="INC_COMMON_CSS" value="true" />
    <%@ include file="/inc/headpro.inc"%>
	<%@ include file="/pages/guide/netbar/top/guide_bar_css_js.jsp"%>
  		<title>${domainIdentified["siteName_fillinfo"]} - ${requestScope.host.name}</title>
	</head>
	<body id="dashboardPage" class="home" g="999_999">
		<c:set var="channel" value="首页" />
		<c:set var="cleanpage" value="ture" /> 
		<%@ include	file="/inc/header.inc"%>
		<%@ include	file="/inc/wrapper.inc"%>
		<%@ include file="/pages/register/guide_app_menu.jsp"%><%--应用菜单 --%>	
		<%--<%@ include	file="guide_hs_dog.jsp"%>--%>
		<div class="main-page">
			<div class="home-content-holder clearfix">
				<div class="home-body"> 	
					<%@ include file="/views/guide/common/body/guide_recApp.jsp" %>					
					<%@ include file="/pages/guide/netbar/middle/guide_bar_middle.jsp"%>
					<div id="replyDiv" class="reply-notify news-feed" style="display:none"><%-- 异步加载 --%>
						<div class="section-header">
							<h2>新留言及回复<span class="stat" id="gossipReplyCount"></span></h2>
						</div>
						<div id="opilist" class="feed-story"></div>
					</div>							
				</div>
				<div class="home-sidebar">   
					<%@ include file="/pages/register/guide_manage_page.jsp" %>  
               		<%@ include file="/pages/register/guide_usercount.jsp" %>  									
         			<%@ include file="/pages/register/guide_footprint.jsp" %><%--最近来访部分--%>          	  
         			<%@ include file="/pages/guide/netbar/right/guide_right_pages.jsp" %>  
         			<%@ include file="/pages/guide/netbar/right/guide_my_pages.jsp" %> 
         			<%@ include file="/pages/guide/netbar/right/guide_my_friends.jsp" %>
         			<%@ include file="/pages/guide/netbar/right/guide_set_head.jsp" %>  
                </div>              	
			</div>
		</div></div>
		<%@ include file="/inc/footer_guide.inc"%>			
	</body>
</html>
