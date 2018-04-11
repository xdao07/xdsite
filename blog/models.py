from django.db import models
from slugify import slugify
from django.shortcuts import reverse

# Create your models here.

# 文件上传路径(/MEDIA_ROOT/article_picture/文章id/文件名)
def upload_generation_dir(instance, filename):
    name, suffix = filename.rsplit('.', 1)  # 拆开文件和扩展名（如：'图片文件.png'则取'图片文件'和'png'）
    return 'article_picture/{0}-{1}.{2}'.format(instance.id, slugify(name), suffix)

# 文章分类表数据模型
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=999, verbose_name='分类排序（从大到小）')

    class Meta:
        ordering = ['index']
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 标签表数据模型
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名')
    is_display = models.BooleanField(default=True, verbose_name='是否显示（默认是）')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    
    # 返回当前标签下文章数
    def article_count(self):
        return self.article.all().count()

    def __str__(self):
        return self.name

# 文章表数据模型
class Article(models.Model):
    title = models.CharField(max_length=60, verbose_name='文章标题')
    category = models.ForeignKey(Category, related_name='article', verbose_name='分类')
    slug = models.CharField(max_length=200, verbose_name='标题映射链接名')
    abstract = models.TextField(max_length=400, verbose_name='文章摘要')
    content = models.TextField(verbose_name='文章内容')
    picture = models.ImageField(upload_to=upload_generation_dir, blank=True, verbose_name='文章展示图片')
    hits = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐（默认否）')
    publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    tag = models.ManyToManyField(Tag, related_name='article', verbose_name='标签')

    class Meta:
        ordering = ['-publish']
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    # 重写save()方法
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)    # 转标题转换为链接标题格式，如"我的博客"转换为"wo-de-bo-ke"
        super(Article, self).save(*args, **kwargs)

    # 获取文章详情链接URL
    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.id, self.slug])    # reverse()函数通过url别名返回对应的url路径

    def __str__(self):
        return "【{0}】 {1}".format(self.category.name, self.title)

# 评论表数据模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    username = models.CharField(max_length=45, verbose_name='用户名', blank=True)
    email = models.EmailField(verbose_name='邮箱', blank=True)
    url = models.URLField(verbose_name='网址', blank=True)
    publish = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    article = models.ForeignKey(Article, related_name='comment', verbose_name='文章')
    pid = models.IntegerField(verbose_name='父级ID')

    class Meta:
        ordering = ['-publish']
        verbose_name = '留言/评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

# 友情链接表数据模型
class Links(models.Model):
    title = models.CharField(max_length=45, verbose_name='链接标题')
    description = models.CharField(max_length=100, verbose_name='链接描述')
    url = models.URLField(verbose_name='链接网址')
    publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排序（从大到小）')

    class Meta:
        ordering = ['-publish']
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
