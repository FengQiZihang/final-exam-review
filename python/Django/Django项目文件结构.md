# Django 项目文件结构

## 完整目录结构

```
MyProject/                      # 项目根目录
│
├── manage.py                   # Django 管理脚本
│
├── MyProject/                  # 项目配置目录（与项目同名）
│   ├── __init__.py
│   ├── settings.py             # 项目配置文件
│   ├── urls.py                 # 项目主路由
│   ├── asgi.py
│   └── wsgi.py
│
├── App1/                       # 应用目录
│   ├── __init__.py
│   ├── admin.py                # 后台管理配置
│   ├── apps.py                 # 应用配置
│   ├── models.py               # 数据模型
│   ├── views.py                # 视图函数
│   ├── urls.py                 # 应用路由（需手动创建）
│   ├── migrations/             # 数据库迁移文件
│   │   └── __init__.py
│   └── templates/              # 应用模板目录（可选）
│       └── App1/
│           └── detail.html
│
├── templates/                  # 全局模板目录
│   ├── base.html               # 父模板（基础模板）
│   └── index.html              # 首页模板
│
├── static/                     # 静态文件目录
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       └── logo.png
│
└── db.sqlite3                  # SQLite 数据库文件
```

---

## 核心文件内容示例

### 1. settings.py（关键配置）

```python
# 注册应用
INSTALLED_APPS = [
    'simpleui',           # UI美化（可选）
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App1',               # 自定义应用
]

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 全局模板目录
        'APP_DIRS': True,
        # ...
    },
]

# 中文设置
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

# 静态文件
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

### 2. urls.py（项目主路由）

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App1.urls')),  # 包含应用路由
]
```

### 3. App1/urls.py（应用路由）

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
]
```

### 4. App1/views.py（视图函数）

```python
from django.shortcuts import render
from .models import App1Model

def index(request):
    items = App1Model.objects.all()
    return render(request, 'index.html', {'items': items})

def detail(request, id):
    item = App1Model.objects.get(id=id)
    return render(request, 'App1/detail.html', {'item': item})
```

---

## 模板继承示例

### base.html（父模板）

```html
{% load static %}
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}我的网站{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- 导航栏 -->
    <nav>
        <a href="{% url 'index' %}">首页</a>
    </nav>

    <!-- 主要内容区域 -->
    <main>
        {% block content %}{% endblock %}
    </main>

    <!-- 页脚 -->
    <footer>
        <p>&copy; 2026 我的网站</p>
    </footer>

    <script src="{% static 'js/main.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### index.html（子模板 - 首页）

```html
{% extends 'base.html' %}

{% block title %}首页 - 我的网站{% endblock %}

{% block content %}
<h1>欢迎来到首页</h1>

<ul>
{% for item in items %}
    <li>
        <a href="{% url 'detail' id=item.id %}">{{ item.name }}</a>
    </li>
{% empty %}
    <li>暂无数据</li>
{% endfor %}
</ul>
{% endblock %}
```

### App1/detail.html（子模板 - 详情页）

```html
{% extends 'base.html' %}

{% block title %}{{ item.name }} - 详情{% endblock %}

{% block content %}
<h1>{{ item.name }}</h1>
<p>性别：{{ item.gender }}</p>
<a href="{% url 'index' %}">返回首页</a>
{% endblock %}
```

---

## 模板继承关系图

```
base.html (父模板)
    │
    ├── index.html (首页)
    │
    └── App1/detail.html (详情页)
```

**继承要点：**
1. 子模板使用 `{% extends 'base.html' %}` 继承父模板
2. 父模板用 `{% block 名称 %}{% endblock %}` 定义可替换区域
3. 子模板用 `{% block 名称 %}内容{% endblock %}` 替换对应区域
