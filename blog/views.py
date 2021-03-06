from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.db.models import Q  # filter(~Q(name=''))过滤表示不等于
from django.http import HttpResponse
from .models import Category, Tag, Article, Comment, Links
from .cache_manager import cache_sync

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

# 文章详情页视图
def article_detail(request, id, slug):
    # 返回匹配id和slug的文章对象，否则的404错误
    article = get_object_or_404(Article, id=id, slug=slug)
    # 更新当前文章点击次数
    article.update_hits()
    return render(request, 'blog/article.html', locals())

# 文章列表页视图
def article_list(request, category_id=None, tag_id=None, page=1):
    # 同步缓存和数据库中的文章点击次数
    cache_sync.syn_article_hits()

    # 从配置文件中获取每页显示文章数
    per_page = settings.PER_PAGE
    # 根据url中匹配的值，判断是文章类目列表还是标签文章列表
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        articles_list = Article.objects.filter(category_id=category_id)
    else:
        tag = get_object_or_404(Tag, id=tag_id)
        articles_list = tag.article.all()

    # 实例化分页对象
    paginator = Paginator(articles_list, per_page)
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    # 当前页（某一页/第一页/最后一页）的所有文章记录对象
    articles = current_page.object_list

    return render(request, 'blog/articlelist.html', locals())

# 同步缓存和数据库中的文章点击次数
def sync_hits_cache_to_db(request):
    cache_sync.syn_article_hits()
    # 返回指定字符串到客户端
    return HttpResponse('Sync hits between cache and db.')