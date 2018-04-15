# -*- encoding: utf-8 -*-
from blog.models import Article
from django.shortcuts import get_object_or_404
from django.core.cache import cache


def syn_article_hits():
    """将redis缓存中的点击次数同步到数据库中"""
    for key in cache.keys("article:*:views"):
        # 从key中获取文章id值
        article_id = int(key.split(':')[1])
        try:
            article = get_object_or_404(Article, id=article_id)
            # 如果数据库中的点击次数大于缓存的值，则更新缓存中的值，否则将缓存中的值存入数据库中
            if article.hits > int(cache.get(key)):
                cache.set(key, article.hits)
            else:
                article.hits = int(cache.get(key))
                article.save()
        except:
            # 数据库中已不存在该文章则redis删除该键
            cache.delete(key)

