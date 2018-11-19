from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from .models import Person
from .forms import addPersonForm

# Create your views here.
def getPersoninfo(request):
    #WebService接口，返回json格式数据 参考https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
    objs = Person.objects.all().values()
    personlist = list(objs)

    return JsonResponse({"data":personlist}, safe=False)
    #return render(request,"HR/personInfo.html")

#new Person to Added
def addPersonInfo(request):
    if request.method=="POST":
        form = addPersonForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/success/")
        pass
    else:
        form = addPersonForm()
    return render(request,'HR/addPersonInfo.html',{'form': form})