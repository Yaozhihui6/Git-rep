"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from Webcar.views import logins,logouts,dashboard,main,order,personalcenter,register
from Webcar.views import editpersonal,editpassword,subscribe

urlpatterns = [
    path('admin/', admin.site.urls,name = '管理员'),
    path('', logins,name = '登录'),
    path('logout/', logouts,name = '登出'),
    path('register/',register,name = '注册'),
    path('main/dashboard/',dashboard,name = '轮盘'),
    path('main/',main,name = '主界面'),
    path('main/order/',order,name = '订单'),
    path('main/subscribe/',subscribe,name = '预约'),
    path('personalcenter/',personalcenter,name = '个人信息'),
    path('editpersonal/',editpersonal,name = '编辑个人信息'),
    path('editpassword/',editpassword,name = '修改密码'),
]
