
from django.shortcuts import render
from .GlobalVar import company

#这是网站的主页地址
def HomePage(request):
    c = company()
    c.ENShortName ="XDL"
    c.CNShortName = "A佰钧成"
    c.CNFullName = "X武汉佰钧成技术有限责任公司X"
    return render(request,"HomePage.html",{"corp":c})

#登录注册验证
def login(request):
    return render(request,"login.html")