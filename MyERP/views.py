
from django.shortcuts import render
from .GlobalVar import company,MessageIn
from .models import Organization
from django.views.generic.edit import CreateView,UpdateView
from .forms import OrganizationForm
from HR.models import Employee

#这是网站的主页地址
def HomePage(request):
    c = company()
    c.ENShortName ="BJC"
    c.CNShortName = "A佰钧成"
    c.CNFullName = "X武汉佰钧成技术有限责任公司X"

    #测试一个用户，查询出该登录用户有几条未读的消息
    admin=Employee.objects.get(pk=7)
    msgList = admin.inSender.all()

    return render(request,"HomePage.html",{"corp":c,  "msgList":msgList})

#登录注册验证
def login(request):
    return render(request,"login.html")

def success(request):
    return render(request,"success.html")

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "OrganizationUpdateView.html"