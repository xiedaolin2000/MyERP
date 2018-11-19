from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Person

# Create your views here.
# 这是WebService接口返回Json格式
def getPersoninfo(request):
    #WebService接口，返回json格式数据 参考https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
    #动态获取列字段，和列字段对应的名字
    colMapping = {}
    for f in Person._meta.fields:
        colMapping[f.name] = f.verbose_name
    l= list(colMapping.keys())
    objs = Person.objects.all().values(*l)
    print(colMapping)
    personlist = list(objs)
    return JsonResponse({"data":personlist}, safe=False)
    #return render(request,"HR/personInfo.html")


def personListview(request):
    pl = Person.objects.all()
    return render(request,"HR/personInfo2Table.html",{"person_list":pl})