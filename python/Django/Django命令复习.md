# Django 命令复习

## 一、项目创建与管理

### 1. 安装 Django
```bash
pip install django
```

### 2. 创建项目
```bash
django-admin startproject 项目名
```
例如：`django-admin startproject Demo`

### 3. 启动项目
```bash
python manage.py runserver 127.0.0.1:8001
```
- 默认地址：`127.0.0.1:8000`
- 可自定义端口：`python manage.py runserver 8080`

---

## 二、数据库迁移

### 1. 生成迁移文件
```bash
python manage.py makemigrations
```
- 指定应用：`python manage.py makemigrations App1`

### 2. 执行迁移
```bash
python manage.py migrate
```
- 指定应用：`python manage.py migrate App1`

---

## 三、用户管理

### 创建超级用户
```bash
python manage.py createsuperuser
```
- 访问管理后台：`http://127.0.0.1:8001/admin/`

---

## 四、应用管理

### 1. 创建应用
```bash
python manage.py startapp 应用名
```
例如：`python manage.py startapp App1`

### 2. 注册应用
在 `settings.py` 中添加：
```python
INSTALLED_APPS = [
    # ...
    'App1',
]
```

---

## 五、配置设置 (settings.py)

### 1. 设置中文
```python
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
```

### 2. 安装 SimpleUI（美化后台）
```bash
pip install django-simpleui
```
在 `settings.py` 中添加：
```python
INSTALLED_APPS = [
    'simpleui',  # 放在最前面
    # ...
]
```

---

## 六、命令速查表

| 功能 | 命令 |
|------|------|
| 安装 Django | `pip install django` |
| 创建项目 | `django-admin startproject 项目名` |
| 创建应用 | `python manage.py startapp 应用名` |
| 生成迁移 | `python manage.py makemigrations` |
| 执行迁移 | `python manage.py migrate` |
| 创建超级用户 | `python manage.py createsuperuser` |
| 启动服务器 | `python manage.py runserver` |
