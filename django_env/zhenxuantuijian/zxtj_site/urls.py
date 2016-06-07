"""zhenxuantuijian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from zxtj_site.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    # 映射到归档页面
    url(r'^archive/', archive, name='archive'),
    # 映射到文章页面
    url(r'^article/$', article, name='article'),
    # 映射到提交评论页面
    url(r'^comment/post/$', comment_post, name='comment_post'),
    # 映射到标签页面
    url(r'^tag/', tag, name='tag'),
    # 映射到分类页面
    url(r'^category/$', category, name='category'),
    # 登录注册注销
    url(r'^logout$', do_logout, name='logout'),
    url(r'^login$', do_login, name='login'),
    url(r'^reg$', do_reg, name='reg'),
]
