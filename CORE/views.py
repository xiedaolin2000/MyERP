
from django.shortcuts import render
from .models import Organization,MessageIn,company
from django.views.generic.edit import UpdateView
from .forms import OrganizationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#这是网站的主页地址,需要登录
@login_required
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

    
