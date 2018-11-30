
from django.shortcuts import render
from .models import Organization,MessageIn,company
from django.views.generic.edit import CreateView,UpdateView
from .forms import OrganizationForm
from HR.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,LogoutView

#这是网站的主页地址
def HomePage(request): 
    return render(request,"HomePage.html")

#登录注册验证
def login(request):
    return render(request,"login.html")

def success(request):
    return render(request,"success.html")

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "OrganizationUpdateView.html"

# 登录视图 LoginView https://docs.djangoproject.com/en/2.1/topics/auth/default/#django.contrib.auth.views.LoginView
class UserLoginView(LoginView):
    template_name="login.html"
    
