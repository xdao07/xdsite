# xdsite
使用Django 框架开发的个人博客项目
***
# 项目介绍
***
### 1、环境
#### 1.1 python3
#### 1.2 Mysql
#### 1.3 Redis
### 2、获取项目
>git clone https://github.com/xdao07/xdsite.git
或者
https://github.com/xdao07/xdsite/archive/master.zip
### 3、安装项目requirements.txt
>pip install -r xdsite/requirements.txt
### 4、创建项目数据库
>mysql -uroot -p -e "CREATE database db_xdsite DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;"
### 5、项目settings.py配置
>DATABASES =
CACHES =

>\# 导航【技术杂谈】分类id列表
NAV_JSZT_CATEGORY = (1, 2, 3, 4, 5)
\# 导航【生活随笔】分类id列表
NAV_SHSB_CATEGORY = (6, 7)
\# 分页，每页显示记录条数
PER_PAGE = 2

>\# 网站基本信息
SITE_NAME = u'Django站点名'
SITE_HTTP = u'http://www.example.net'
SITE_DESC = u'Django站点描述'
SITE_KEYWORDS = u'Django站点关键字'
SITE_BEIAN = u'粤ICP备11111111号'
PRO_EMAIL = u'admin@example.cn'
### 6、初始化数据库
>python manage.py makemigrations
python manage.py migrate
### 7、创建Admin后台管理用户
>python manage.py createsuperuser
### 8、运行项目
>python manage.py runserver
### 9、浏览器中测试项目
>http://127.0.0.1:8000/  
### 10、Admin后台添加数据
>http://127.0.0.1:8000/admin/