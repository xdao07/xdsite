from django.shortcuts import render
from django.conf import settings
from django.db.models import Q  # filter(~Q(name=''))过滤表示不等于
from .models import Category, Tag, Article, Comment, Links

def global_setting(request):
    """
    定义全局变量函数，将函数中的变量通过locals()返回
    将global_setting函数加到 settings.py/TEMPLATES/OPTIONS 的上下文处理器中
    """
    # 获取所有可以显示的标签对象
    tags = Tag.objects.filter(is_display=1).all()
    # 获取所有友情链接对象
    links = Links.objects.all()

    # 图文推荐文章列表对象
    recommend_articles = Article.objects.filter(~Q(picture='')).filter(is_recommend=1).order_by('-hits')[:5]

    # 点击排行版文章列表对象
    hits_articles = Article.objects.order_by('-hits')[:10]

    # 定义导航分类
    # 从数据库获取指定ID的分类对象列表（置于技术杂谈导航下）
    nav_jszt_category = Category.objects.filter(id__in=settings.NAV_JSZT_CATEGORY).order_by('-index')

    # 从数据库获取指定ID的分类对象列表（置于生活随笔导航下）
    nav_shsb_category = Category.objects.filter(id__in=settings.NAV_SHSB_CATEGORY).order_by('-index')

    # settings中站点基本信息配置
    site_name = settings.SITE_NAME
    site_http = settings.SITE_HTTP
    site_keywords = settings.SITE_KEYWORDS
    site_desc = settings.SITE_DESC
    site_beian = settings.SITE_BEIAN

    pro_mail = settings.PRO_EMAIL

    return locals()

# 首页视图
def index(request):
    articles = Article.objects.all()

    return render(request, 'blog/index.html', locals())


