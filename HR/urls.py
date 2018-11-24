"""MyERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from .views import getEmployeeinfo, addEmployeeInfo,modEmployeeInfo
from .views import EmployeeListView
from .views import EmployeeCreateView,EmployeeDeleteView,EmployeeUpdateView

urlpatterns = [
    #WebService 接口
    path('WS', getEmployeeinfo),
    path('', EmployeeListView.as_view()),
    path('add/',         EmployeeCreateView.as_view(), name="Employee-add"),
    path('<int:pk>/',    EmployeeUpdateView.as_view(), name="Employee-update"),
    path('<int:pk>/del', EmployeeDeleteView.as_view(), name="Employee-delete"),
]
