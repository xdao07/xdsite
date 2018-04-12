from django.contrib import admin
from .models import Category, Tag, Article, Comment, Links

# Register your models here.

# 使用装饰器注册模型
# Category模型管理器
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'index')
    search_fields = ('name',)
    list_editable = ('index',)

# Tag模型管理器
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_display')
    list_filter = ('is_display',)
    list_editable = ('is_display',)

# Article模型管理器
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = ('id', 'slug', 'publish')
    list_display = ('title', 'slug', 'hits', 'is_recommend', 'publish', 'category')
    filter_horizontal = ('tag',)
    list_editable = ('hits', 'is_recommend',)
    list_filter = ('category',)
    date_hierarchy = 'publish'

    # 将指定的静态素材应用于当前表单中
    class Media:
        css = {}
        js = (
            '/static/blog/js/kindeditor-4.1.11-zh-CN/kindeditor-all-min.js',
            '/static/blog/js/kindeditor-4.1.11-zh-CN/plugins/code/code.js',   # 覆盖kindeditor-all-min.js中的相同部分
            '/static/blog/js/kindeditor-4.1.11-zh-CN/config.js',
            '/static/blog/js/kindeditor-4.1.11-zh-CN/lang/zh-CN.js',
        )

# Comment模型管理器
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'article', 'pid', 'publish')

# Links模型管理器
@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'publish', 'index')
    list_editable = ('url', 'index')

