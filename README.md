# Блог на Django.
---

## English

### Install

```
git clone https://github.com/python3django/django-blog.git
cd django-blog/
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

### Usage

```
python manage.py runserver
```

#### Follow the link

```
http://127.0.0.1:8000/blog/
```

### Database

PostgreSQL is used as a database. Blog search is implemented using PostgreSQL functionality.

#### Account application

The account app implements the standard Django functionality for registration and authentication.

#### Blog app

The blog application implements the functionality of a blog: a list of posts, a page for a single post, comments. As well as sitemap, RSS feed, tag functionality.

#### API

blog/api/ - API Django RESTfull.

## Russian

### Установка

```
git clone https://github.com/python3django/django-blog.git
cd django-blog/
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

### Запуск

```
python manage.py runserver
```

#### Переходим по ссылке

```
http://127.0.0.1:8000/blog/
```

### База данных

В качестве базы данных используется PostgreSQL. Поиск по блогу реализован с использованием функционала PostgreSQL.

#### Приложение account

Приложение account реализует стандартный функционал Django для регистрации и аутентификации.

#### Приложение blog

Приложение blog реализует функционал блога: список постов, страница отдельного поста, комментарии. А также sitemap, RSS канал, функционал тегов.

В качестве базы данных используется PostgreSQL. Поиск по блогу реализован с использованием функционала PostgreSQL.

#### API

blog/api/ - API Django RESTfull.
