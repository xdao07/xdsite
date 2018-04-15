# -*- encoding: utf-8 -*-
from django.core.cache import cache

def update_article_hits(article):
    """更新文章点击次数"""
    # 指定key不存在则从数据库hits字段添加，并设置永不过期
    cache.add("article:{}:views".format(article.id), article.hits, timeout=None)

    # 指定key的值自增1
    cache.incr("article:{}:views".format(article.id))

def get__article_hits(article):
    """获取文章点击次数"""
    # 指定key不存在则从数据库hits字段添加，并设置永不过期
    cache.add("article:{}:views".format(article.id), article.hits, timeout=None)

    return cache.get("article:{}:views".format(article.id))
