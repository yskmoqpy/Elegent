"""bms URL Configuration

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
#from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
  #  path('$', views.login),
    path('pub_list/', views.publisher_list),      # 出版社列表
    path('add_pub/', views.add_publisher),     # 新增出版社
    path('edit_pub/', views.edit_publisher),     # 编辑出版社
    path('drop_pub/', views.drop_publisher),     # 删除出版社
    path('author_list/', views.author_list),     # 作者列表
    path('add_author/', views.add_author),    # 新增作者
    path('drop_author/', views.drop_author),    # 删除作者
    path('edit_author/', views.edit_author),    # 编辑作者
    path('book_list/', views.book_list),     # 图书列表
    path('add_book/', views.add_book),     # 新增图书
    path('drop_book/', views.drop_book),     # 删除图书
    path('edit_book/', views.edit_book),     # 编辑图书
    path('login/', views.login),     # 登录动作
    path('signup/', views.register),     # 注册页面
    path('register/', views.register),     # 注册
]
