from django.conf.urls import url
from django.views.generic import TemplateView   # 通用视图，可直接将静态映射为视图函数

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='blog/index.html'), name='home'),
    url(r'^aboutme/$', TemplateView.as_view(template_name='blog/aboutme.html'), name='aboutme'),
    url(r'^messageme/$', TemplateView.as_view(template_name='blog/messageme.html'), name='messageme'),
    url(r'^articlelist/$', TemplateView.as_view(template_name='blog/articlelist.html'), name='articlelist'),
    url(r'^article/$', TemplateView.as_view(template_name='blog/article.html'), name='article'),
]
