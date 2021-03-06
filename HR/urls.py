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
from . import views
from .views import getEmployeeinfo, modEmployeeInfo
from .views import EmployeeListView, BackBoneCreateView
from .views import EmployeeCreateView,EmployeeDeleteView,EmployeeUpdateView,EmployeeDetailView,QueryResultListView
from .views import DemissionCreateView,DemissionUpdateView

urlpatterns = [
    #WebService 接口
    path('WS', getEmployeeinfo),
    path('',             QueryResultListView.as_view(), name="HR-Root"),
    path('list',         EmployeeListView.as_view(),    name="Employee-list"),
    path('add/',         EmployeeCreateView.as_view(),  name="Employee-add"),
    path('<int:pk>/',    EmployeeDetailView.as_view(),  name="Employee-detail"),
    path('<int:pk>/upd', EmployeeUpdateView.as_view(),  name="Employee-update"),
    path('<int:pk>/del', EmployeeDeleteView.as_view(),  name="Employee-delete"),
    #骨干员工
    path('bone/',        BackBoneCreateView.as_view(),  name="BackBone-add"),
    #离职手续
    path('leave/',         DemissionCreateView.as_view(), name="Demission-add"),
    path('<int:pk>/leave', DemissionUpdateView.as_view(), name="Demission-update"),
]
