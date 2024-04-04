# Django REST GraphQL E-commerce Project

![E-commerce](https://img.shields.io/badge/E--commerce-Django-brightgreen)

Этот проект - пример веб-приложения электронной коммерции, разработанного с использованием Django REST Framework и GraphQL.

## Описание проекта

Проект представляет собой полнофункциональное веб-приложение для электронной коммерции, где пользователи могут просматривать и покупать товары, администраторы могут управлять категориями, продуктами и новостями.

## Установка и Запуск

1. **Клонирование репозитория**

    ```bash
    git clone https://github.com/Adik8712/Django-REST-GraphQL-E-commerce-Project.git
    cd Django-REST-GraphQL-E-commerce-Project/
    ```

2. **Установка виртуального окружения**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # для Linux / macOS
    venv\Scripts\activate  # для Windows
    ```

3. **Установка зависимостей**

    ```bash
    pip install -r requirements.txt
    ```

4. **Настройка базы данных**

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

5. **Создание административного аккаунта**

    ```bash
    python3 manage.py createsuperuser
    ```

6. **Запуск сервера**

    ```bash
    python3 manage.py runserver
    ```

7. **Доступ к приложению**

    После запуска сервера перейдите по адресу [http://localhost:8000](http://localhost:8000) для доступа к приложению.

## Структура проекта

- `api_main`: Приложение Django для REST API, включающее представления, модели, сериализаторы и URL-адреса.
- `graphqlapi`: Приложение Django для GraphQL, содержащее схему и настройки.
- `main`: Основное приложение Django, содержащее основные модели, представления и шаблоны.
- `ProductSlugApi`: Основной модуль Django с настройками проекта и URL-адресами.
- `static` и `templates`: Директории для статических файлов и HTML-шаблонов.

## Структура проекта

```
.
├── api_main
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── serializers.cpython-310.pyc
│   │   ├── serializers.cpython-311.pyc
│   │   ├── views.cpython-310.pyc
│   │   └── views.cpython-311.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── Dockerfile
├── Dockerfile1
├── git.sh
├── graphqlapi
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── __pycache__
│   │   ├── apps.cpython-310.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── schema.cpython-310.pyc
│   │   ├── schema.cpython-311.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── urls.cpython-311.pyc
│   ├── schema.py
│   └── urls.py
├── LICENSE
├── main
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_product_slug.py
│   │   ├── 0003_alter_product_options_alter_product_slug.py
│   │   ├── 0004_news.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── urls.cpython-310.pyc
│   │   ├── urls.cpython-311.pyc
│   │   ├── utils.cpython-310.pyc
│   │   ├── utils.cpython-311.pyc
│   │   ├── views.cpython-310.pyc
│   │   └── views.cpython-311.pyc
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── manage.py
├── media
│   └── products
│       ├── 12image.jpg.jpg
│       ├── 9image.jpg.jpg
│       ├── gettyimages-1314489757-612x612.jpg
│       ├── images.jpeg
│       └── istockphoto-1319763895-612x612.jpg
├── plaintext.tree
├── ProductSlugApi
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── logging.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── settings.cpython-311.pyc
│   │   ├── urls.cpython-310.pyc
│   │   ├── urls.cpython-311.pyc
│   │   ├── wsgi.cpython-310.pyc
│   │   └── wsgi.cpython-311.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── requirements.txt
├── static
│   └── main.css
├── templates
│   ├── index.html
│   └── product_detail.html
└── venv
    ├── bin
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── activate.nu
    │   ├── activate.ps1
    │   ├── activate_this.py
    │   ├── django-admin
    │   ├── pip
    │   ├── pip3
    │   ├── pip-3.11
    │   ├── pip3.11
    │   ├── python -> /usr/bin/python3
    │   ├── python3 -> python
    │   ├── python3.11 -> python
    │   ├── sqlformat
    │   ├── wheel
    │   ├── wheel3
    │   ├── wheel-3.11
    │   └── wheel3.11
    ├── lib
    │   └── python3.11
    └── pyvenv.cfg

23 directories, 112 files

```

### Участники

- [Adik](https://github.com/Adik8712)

### Лицензия

Этот проект лицензирован по лицензии MIT - см. файл [LICENSE](LICENSE) для получения дополнительной информации.

---

Не стесняйтесь вносить свой вклад в проект, открывая проблемы или отправляя запросы на объединение изменений (pull requests)! Если у вас возникли проблемы или есть предложения по улучшению, пожалуйста, дайте [нам](https://t.me/AdikPy) знать. Удачного кодирования! 🚀