from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from .models import Person
from .forms import addPersonForm

# Create your views here.
# 这是WebService接口返回Json格式
def getPersoninfo(request):
    #WebService接口，返回json格式数据 参考https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
    #动态获取列字段，和列字段对应的名字
    colMapping = {}
    for f in Person._meta.fields:
        colMapping[f.name] = f.verbose_name
    l= list(colMapping.keys())
    # objs = Person.objects.all().values(*l)
    #只显示在职人员
    objs = Person.objects.filter(workStatus="00").values(*l)
    # print(colMapping)
    personlist = list(objs)

    return JsonResponse({"data":personlist}, safe=False)
    #return render(request,"HR/personInfo.html")

def personList(request):
    return render(request,"HR/personInfo2Table.html")

#new Person to Added
def addPersonInfo(request):
    if request.method=="POST":
        form = addPersonForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # p = addPersonForm(form.cleaned_data)
            # p.save()
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/success/")
        pass
    else:
        form = addPersonForm()
    return render(request,'HR/addPersonInfo.html',{'form': form})
