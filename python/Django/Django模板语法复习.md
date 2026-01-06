# Django 模板语法复习

> ⚠️ **考试重点**：模板继承、语法速查表

---

## 一、模板基础

### 1. 模板位置
在应用目录下创建 `templates` 文件夹，或在项目根目录创建并配置：
```python
# settings.py
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
        # ...
    },
]
```

### 2. 渲染模板
```python
# views.py
from django.shortcuts import render

def index(request):
    context = {'name': '张三', 'age': 20}
    return render(request, 'index.html', context)
```

---

## 二、变量语法

### 1. 输出变量
```django
{{ 变量名 }}
```
例如：
```django
<p>姓名：{{ name }}</p>
<p>年龄：{{ age }}</p>
```

### 2. 访问属性/方法
```django
{{ 对象.属性 }}
{{ 对象.方法 }}
{{ 列表.0 }}
{{ 字典.键名 }}
```

---

## 三、标签语法

### 1. 条件判断
```django
{% if 条件 %}
    内容
{% elif 条件2 %}
    内容2
{% else %}
    其他内容
{% endif %}
```

### 2. 循环遍历
```django
{% for item in 列表 %}
    {{ item }}
{% empty %}
    列表为空时显示
{% endfor %}
```

**循环变量：**
| 变量 | 说明 |
|------|------|
| `forloop.counter` | 当前迭代次数（从1开始） |
| `forloop.counter0` | 当前迭代次数（从0开始） |
| `forloop.first` | 是否是第一次迭代 |
| `forloop.last` | 是否是最后一次迭代 |

### 3. URL 反向解析
```django
{% url 'url名称' 参数 %}
```
例如：
```django
<a href="{% url 'detail' id=1 %}">详情</a>
```

### 4. 静态文件
```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'images/logo.png' %}">
```

### 5. 模板继承
**父模板 (base.html)：**
```django
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}默认标题{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

**子模板：**
```django
{% extends 'base.html' %}

{% block title %}页面标题{% endblock %}

{% block content %}
    <h1>页面内容</h1>
{% endblock %}
```

### 6. 包含模板
```django
{% include 'header.html' %}
```

---

## 四、过滤器语法

### 基本格式
```django
{{ 变量|过滤器 }}
{{ 变量|过滤器:参数 }}
```

### 常用过滤器

| 过滤器 | 说明 | 示例 |
|--------|------|------|
| `length` | 获取长度 | `{{ list|length }}` |
| `default` | 默认值 | `{{ value|default:"无" }}` |
| `date` | 日期格式化 | `{{ date|date:"Y-m-d" }}` |
| `truncatechars` | 截断字符 | `{{ text|truncatechars:20 }}` |
| `safe` | 不转义 HTML | `{{ html|safe }}` |
| `upper` | 转大写 | `{{ name|upper }}` |
| `lower` | 转小写 | `{{ name|lower }}` |
| `join` | 连接列表 | `{{ list|join:", " }}` |
| `add` | 加法 | `{{ num|add:10 }}` |

---

## 五、语法速查表

| 类型 | 语法 | 示例 |
|------|------|------|
| 变量 | `{{ }}` | `{{ name }}` |
| 标签 | `{% %}` | `{% if %}...{% endif %}` |
| 注释 | `{# #}` | `{# 这是注释 #}` |
| 过滤器 | `|` | `{{ name|upper }}` |
