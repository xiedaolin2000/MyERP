from django.shortcuts import render
from django.http import JsonResponse
from .models import Person

# Create your views here.
def getPersoninfo(request):
    #WebService接口，返回json格式数据 参考https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
    objs = Person.objects.all().values()
    personlist = list(objs)
    return JsonResponse({"data":personlist}, safe=False)
    #return render(request,"HR/personInfo.html")
