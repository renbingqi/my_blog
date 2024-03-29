"""my_blog URL Configuration

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
from django.urls import path, re_path
from article import views
urlpatterns = [
    path('',views.article_list,name='article_list'),
    path('create',views.article_create,name='article_create'),
    path('delete/<int:id>',views.article_delete,name='article_delete'),
    path('update/<int:id>',views.article_update,name='article_update'),
    path('update_hot/<int:id>',views.updatehot,name='updatehot'),
    path('upload_picture',views.upload_picture,name='upload_picture'),
    path('get_file',views.get_file,name='get_picture')
]
