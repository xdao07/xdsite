from django.conf.urls import url
from django.views.generic import TemplateView   # 通用视图，可直接将静态映射为视图函数
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^aboutme/$', TemplateView.as_view(template_name='blog/aboutme.html'), name='aboutme'),
    url(r'^messageme/$', TemplateView.as_view(template_name='blog/messageme.html'), name='messageme'),
    url(r'^article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail, name='article_detail'),    # 将正则匹配的id和slug传递给视图函数
    url(r'^article-list/(?P<category_id>\d+)/$', views.article_list, name='article_list'),    # 通过导航进入的列表没有page参数，则使用视图函数的默认值page=1
    url(r'^article-list/(?P<category_id>\d+)/(?P<page>\d)/$', views.article_list, name='article_list'),
    url(r'^article-list/(tag)/(?P<tag_id>\d+)/$', views.article_list, name='article_list'),    # 通过标签链接进入的列表没有page参数，则使用视图函数默认值page=1，注意标签页列表路径含有/tag/
    url(r'^article-list/(tag)/(?P<tag_id>\d+)/(?P<page>\d)/$', views.article_list, name='article_list'),
    # 通过指定路由到指定视图将执行同步函数
    url(r'^sync-hits-cache-to-db/$', views.sync_hits_cache_to_db, name='sync_hits_cache_to_db'),
]
