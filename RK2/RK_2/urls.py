"""RK_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from App import views as app_views

router = routers.DefaultRouter()
router.register(r'books', app_views.BookViewSet)
router.register(r'chapters', app_views.ChapterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('app/bookslist', app_views.BookList),
    path('app/chapterslist', app_views.ChapterList),
    path('app/bookslist/<int:book_id>', app_views.BookDetail, name='book_detail'),
    path('app/chapterslist/<int:chapter_id>', app_views.ChapterDetail, name='chapter_detail')
]
