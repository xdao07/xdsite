"""
Django settings for xdsite project.

Generated by 'django-admin startproject' using Django 1.10.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7tmz(13@)v@s(f$4dk7^7qb^l_ng$y&fh@^$d2z(l^h-ub(=yz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'xdsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],    # 指定模板位置位于根目录下的templates目录
        'APP_DIRS': True,    # 是否可以APP下的templates目录作为模板目录
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.views.global_setting',   # 将global_setting中定义的全局变量加入上下文处理器中
            ],
        },
    },
]

WSGI_APPLICATION = 'xdsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_xdsite',
        'HOST': '192.168.100.1',
        'PORT': '3306',
        'USER': 'webapp',
        'PASSWORD': 'web123456app',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'    # 设置中文

TIME_ZONE = 'Asia/Shanghai'    # 设置时区

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')    # 指定静态文件存放目录
]

# 媒体文件配置
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# 允许上传文件类型['jpg', 'png', 'jpeg']
ALLOW_SUFFIX = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'txt', 'html']

"""
自定义变量
"""
# 导航【技术杂谈】分类id列表
NAV_JSZT_CATEGORY = (1, 2, 3, 4, 5)
# 导航【生活随笔】分类id列表
NAV_SHSB_CATEGORY = (6, 7)
# 分页，每页显示记录条数
PER_PAGE = 2

# 网站基本信息
SITE_NAME = u'Django个人博客——江南墨卷'
SITE_HTTP = u'http://www.example.net'
SITE_DESC = u'天将降大任于是人也，必先苦其心志，劳其筋骨，饿其体肤，空乏其身，行拂乱其所为，所以动心忍性，曾益其所不能。'
SITE_KEYWORDS = u'运维，开发，Linux，数据库'
SITE_BEIAN = u'粤ICP备11111111号'
PRO_EMAIL = u'admin@example.cn'
