
from django.shortcuts import render

#这是网站的主页地址
def HomePage(request):
    return render(request,"HomePage.html")

#登录注册验证
def login(request):
    return render(request,"login.html")