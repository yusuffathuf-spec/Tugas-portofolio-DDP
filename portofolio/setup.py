#!/usr/bin/env python3
"""
Script untuk membuat struktur folder dan file Django Profile Web
Jalankan dengan: python setup_project.py
"""

import os
import sys

def create_file(path, content):
    """Membuat file dengan konten"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Created: {path}")

def main():
    print("=== Membuat Struktur Project Django Profile ===\n")
    
    # Struktur folder
    folders = [
        "myprofile",
        "myprofile/myprofile",
        "myprofile/portfolio",
        "myprofile/portfolio/templates",
        "myprofile/portfolio/static",
        "myprofile/portfolio/static/images",
    ]
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"✓ Created folder: {folder}")
    
    print("\n=== Membuat File-file ===\n")
    
    # 1. myprofile/myprofile/settings.py
    create_file("myprofile/myprofile/settings.py", """import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-your-secret-key-here-change-in-production'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
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

ROOT_URLCONF = 'myprofile.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myprofile.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'id-id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'portfolio/static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
""")

    # 2. myprofile/myprofile/urls.py
    create_file("myprofile/myprofile/urls.py", """from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]
""")

    # 3. myprofile/myprofile/wsgi.py
    create_file("myprofile/myprofile/wsgi.py", """import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myprofile.settings')
application = get_wsgi_application()
""")

    # 4. myprofile/myprofile/__init__.py
    create_file("myprofile/myprofile/__init__.py", "")

    # 5. myprofile/portfolio/urls.py
    create_file("myprofile/portfolio/urls.py", """from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
]
""")

    # 6. myprofile/portfolio/views.py
    create_file("myprofile/portfolio/views.py", """from django.shortcuts import render

def home(request):
    context = {
        'page_title': 'Home',
        'name': 'John Doe',
        'profession': 'Web Developer',
        'description': 'Saya adalah seorang web developer yang passionate dalam menciptakan aplikasi web yang inovatif dan user-friendly.',
        'skills': ['Python', 'Django', 'JavaScript', 'Bootstrap', 'HTML/CSS'],
        'email': 'john.doe@example.com',
        'phone': '+62 812-3456-7890',
        'location': 'Jakarta, Indonesia'
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'page_title': 'About Me',
        'education': [
            {
                'degree': 'S1 Teknik Informatika',
                'institution': 'Universitas Indonesia',
                'year': '2018 - 2022',
                'description': 'Fokus pada pengembangan web dan mobile application'
            },
            {
                'degree': 'SMA IPA',
                'institution': 'SMA Negeri 1 Jakarta',
                'year': '2015 - 2018',
                'description': 'Juara 1 Olimpiade Komputer tingkat Provinsi'
            }
        ],
        'organizations': [
            {
                'name': 'Himpunan Mahasiswa Informatika',
                'position': 'Ketua Divisi IT',
                'period': '2020 - 2021',
                'description': 'Memimpin tim pengembangan website organisasi'
            },
            {
                'name': 'Google Developer Student Club',
                'position': 'Core Team Member',
                'period': '2019 - 2022',
                'description': 'Mengadakan workshop dan training untuk mahasiswa'
            }
        ]
    }
    return render(request, 'about.html', context)

def gallery(request):
    context = {
        'page_title': 'Gallery',
        'images': [
            {
                'title': 'Workshop Web Development',
                'description': 'Mengajar workshop tentang Django Framework',
                'image': 'https://images.unsplash.com/photo-1531482615713-2afd69097998?w=800'
            },
            {
                'title': 'Hackathon Competition',
                'description': 'Tim kami meraih juara 1 di kompetisi hackathon nasional',
                'image': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800'
            },
            {
                'title': 'Tech Conference 2023',
                'description': 'Menjadi speaker di konferensi teknologi',
                'image': 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=800'
            }
        ]
    }
    return render(request, 'gallery.html', context)
""")

    # 7. myprofile/portfolio/__init__.py
    create_file("myprofile/portfolio/__init__.py", "")

    # 8. myprofile/portfolio/apps.py
    create_file("myprofile/portfolio/apps.py", """from django.apps import AppConfig

class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
""")

    # 9. myprofile/portfolio/models.py
    create_file("myprofile/portfolio/models.py", """from django.db import models

# Models untuk future development
""")

    # 10. myprofile/portfolio/admin.py
    create_file("myprofile/portfolio/admin.py", """from django.contrib import admin

# Register your models here.
""")

    # 11. Base Template
    create_file("myprofile/portfolio/templates/base.html", """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Profile{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding-top: 56px;
        }
        
        .navbar {
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .navbar-brand {
            font-weight: bold;
            font-size: 1.5rem;
        }
        
        .nav-link {
            color: white !important;
            margin: 0 10px;
            transition: all 0.3s ease;
        }
        
        .nav-link:hover {
            transform: translateY(-2px);
            color: #f39c12 !important;
        }
        
        .hero-section {
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            padding: 80px 0;
            margin-bottom: 50px;
        }
        
        .card {
            border: none;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            margin-bottom: 30px;
        }
        
        .card:hover {
            transform: translateY(-10px);
        }
        
        .footer {
            background: var(--primary-color);
            color: white;
            padding: 30px 0;
            margin-top: 50px;
        }
        
        .btn-primary {
            background: var(--secondary-color);
            border: none;
            transition: all 0.3s ease;
        }
        
        .btn-primary:hover {
            background: var(--accent-color);
            transform: scale(1.05);
        }
    </style>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top">
        <div class="container">
            <a class="navbar-brand" href="{% url 'portfolio:home' %}">
                <i class="fas fa-user-circle"></i> MyProfile
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'portfolio:home' %}">
                            <i class="fas fa-home"></i> Home
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'portfolio:about' %}">
                            <i class="fas fa-user"></i> About Me
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'portfolio:gallery' %}">
                            <i class="fas fa-images"></i> Gallery
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    {% block content %}{% endblock %}

    <footer class="footer text-center">
        <div class="container">
            <p>&copy; 2024 My Profile. All rights reserved.</p>
            <div class="social-links mt-3">
                <a href="#" class="text-white me-3"><i class="fab fa-facebook fa-2x"></i></a>
                <a href="#" class="text-white me-3"><i class="fab fa-twitter fa-2x"></i></a>
                <a href="#" class="text-white me-3"><i class="fab fa-instagram fa-2x"></i></a>
                <a href="#" class="text-white"><i class="fab fa-linkedin fa-2x"></i></a>
            </div>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
""")

    # 12. Home Template
    create_file("myprofile/portfolio/templates/home.html", """{% extends 'base.html' %}

{% block title %}{{ page_title }} - My Profile{% endblock %}

{% block content %}
<div class="hero-section text-center">
    <div class="container">
        <h1 class="display-3 fw-bold mb-4">Halo, Saya {{ name }}</h1>
        <p class="lead fs-4">{{ profession }}</p>
        <a href="{% url 'portfolio:about' %}" class="btn btn-light btn-lg mt-3">
            Lebih Lanjut <i class="fas fa-arrow-right"></i>
        </a>
    </div>
</div>

<div class="container">
    <div class="row">
        <div class="col-lg-8 mx-auto">
            <div class="card">
                <div class="card-body p-5">
                    <h2 class="card-title mb-4"><i class="fas fa-user-tie text-primary"></i> Tentang Saya</h2>
                    <p class="lead">{{ description }}</p>
                    
                    <h3 class="mt-5 mb-3"><i class="fas fa-code text-primary"></i> Keahlian</h3>
                    <div class="row">
                        {% for skill in skills %}
                        <div class="col-md-6 mb-3">
                            <div class="p-3 bg-light rounded">
                                <i class="fas fa-check-circle text-success"></i> {{ skill }}
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="row mt-5">
        <div class="col-md-4">
            <div class="card text-center">
                <div class="card-body">
                    <i class="fas fa-envelope fa-3x text-primary mb-3"></i>
                    <h5>Email</h5>
                    <p>{{ email }}</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card text-center">
                <div class="card-body">
                    <i class="fas fa-phone fa-3x text-success mb-3"></i>
                    <h5>Telepon</h5>
                    <p>{{ phone }}</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card text-center">
                <div class="card-body">
                    <i class="fas fa-map-marker-alt fa-3x text-danger mb-3"></i>
                    <h5>Lokasi</h5>
                    <p>{{ location }}</p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")

    # 13. About Template
    create_file("myprofile/portfolio/templates/about.html", """{% extends 'base.html' %}

{% block title %}{{ page_title }} - My Profile{% endblock %}

{% block content %}
<div class="hero-section text-center">
    <div class="container">
        <h1 class="display-4 fw-bold">About Me</h1>
        <p class="lead">Riwayat Pendidikan & Organisasi</p>
    </div>
</div>

<div class="container">
    <div class="row">
        <div class="col-lg-10 mx-auto">
            <h2 class="mb-4"><i class="fas fa-graduation-cap text-primary"></i> Riwayat Pendidikan</h2>
            {% for edu in education %}
            <div class="card mb-4">
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-9">
                            <h4 class="card-title text-primary">{{ edu.degree }}</h4>
                            <h5 class="text-muted">{{ edu.institution }}</h5>
                            <p class="mt-3">{{ edu.description }}</p>
                        </div>
                        <div class="col-md-3 text-end">
                            <span class="badge bg-secondary fs-6">{{ edu.year }}</span>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}

            <h2 class="mb-4 mt-5"><i class="fas fa-users text-primary"></i> Pengalaman Organisasi</h2>
            {% for org in organizations %}
            <div class="card mb-4">
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-9">
                            <h4 class="card-title text-primary">{{ org.name }}</h4>
                            <h5 class="text-muted">{{ org.position }}</h5>
                            <p class="mt-3">{{ org.description }}</p>
                        </div>
                        <div class="col-md-3 text-end">
                            <span class="badge bg-success fs-6">{{ org.period }}</span>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</div>
{% endblock %}
""")

    # 14. Gallery Template
    create_file("myprofile/portfolio/templates/gallery.html", """{% extends 'base.html' %}

{% block title %}{{ page_title }} - My Profile{% endblock %}

{% block extra_css %}
<style>
    .gallery-item {
        position: relative;
        overflow: hidden;
        border-radius: 15px;
        cursor: pointer;
    }
    
    .gallery-item img {
        width: 100%;
        height: 300px;
        object-fit: cover;
        transition: transform 0.5s ease;
    }
    
    .gallery-item:hover img {
        transform: scale(1.1);
    }
    
    .gallery-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
        color: white;
        padding: 20px;
        transform: translateY(100%);
        transition: transform 0.3s ease;
    }
    
    .gallery-item:hover .gallery-overlay {
        transform: translateY(0);
    }
</style>
{% endblock %}

{% block content %}
<div class="hero-section text-center">
    <div class="container">
        <h1 class="display-4 fw-bold">Gallery</h1>
        <p class="lead">Dokumentasi Kegiatan & Prestasi</p>
    </div>
</div>

<div class="container">
    <div class="row">
        {% for image in images %}
        <div class="col-md-4 mb-4">
            <div class="gallery-item">
                <img src="{{ image.image }}" alt="{{ image.title }}">
                <div class="gallery-overlay">
                    <h5 class="fw-bold">{{ image.title }}</h5>
                    <p class="mb-0">{{ image.description }}</p>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
    
    <div class="text-center mt-5">
        <div class="card">
            <div class="card-body p-5">
                <h3>Tertarik Bekerja Sama?</h3>
                <p class="lead">Jangan ragu untuk menghubungi saya!</p>
                <a href="mailto:john.doe@example.com" class="btn btn-primary btn-lg">
                    <i class="fas fa-envelope"></i> Hubungi Saya
                </a>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")

    # 15. manage.py
    create_file("myprofile/manage.py", """#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myprofile.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)
""")

    # 16. requirements.txt
    create_file("myprofile/requirements.txt", """Django>=4.2,<5.0
""")

    # 17. README.md
    create_file("myprofile/README.md", """# Django Profile Website

Website profile pribadi sederhana menggunakan Django dan Bootstrap.

## Cara Menjalankan

1. Install Django:
```bash
pip install -r requirements.txt
```

2. Jalankan migrasi:
```bash
python manage.py migrate
```

3. Jalankan server:
```bash
python manage.py runserver
```

4. Buka browser di: http://127.0.0.1:8000

## Fitur

- Home: Profile diri dengan informasi kontak
- About Me: Riwayat pendidikan dan organisasi
- Gallery: Dokumentasi kegiatan dengan hover effect

## Teknologi

- Django 4.2+
- Bootstrap 5.3
- Font Awesome 6.4
- Responsive Design
""")

    print("\n" + "="*50)
    print("✓ SELESAI! Struktur project berhasil dibuat!")
    print("="*50)
    print("\nLangkah selanjutnya:")
    print("1. cd myprofile")
    print("2. pip install -r requirements.txt")
    print("3. python manage.py migrate")
    print("4. python manage.py runserver")
    print("\nBuka browser: http://127.0.0.1:8000")

if __name__ == "__main__":
    main()