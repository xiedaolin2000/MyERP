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
from .views import getPersoninfo, addPersonInfo,modPersonInfo
from .views import PersonListView
from .views import PersonCreateView,PersonDeleteView,PersonUpdateView

urlpatterns = [
    #WebService 接口
    path('WS', getPersoninfo),
    path('', PersonListView.as_view()),
    path('add/',         PersonCreateView.as_view(), name="person-add"),
    path('<int:pk>/',    PersonUpdateView.as_view(), name="person-update"),
    path('<int:pk>/del', PersonDeleteView.as_view(), name="person-delete"),
]
