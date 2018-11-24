from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect,Http404
from .models import Person
from .forms import PersonForm
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

class PersonListView(ListView):
    model = Person
    ordering= ["-id"]
    context_object_name = 'person'
    template_name='HR/PersonListView.html'
    def get_queryset(self):
        #返回在职状态的人员
        return Person.objects.filter(workStatus="00")
class PersonDetailView(DetailView):
    model = Person
    template_name='personDetailView.html'

#通用编辑试图
class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name='HR/PersonCreateView.html'
    success_url = "/success/"
    
class PersonDeleteView(DeleteView):
    model = Person
    context_object_name="person"
    template_name='HR/PersonConfirmDelete.html'
    success_url = "/success/"
    #我们必须在这里使用reverse_lazy()，而不是 reverse(),因为在导入文件时未加载URL
    # success_url = reverse_lazy('author-list')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name='HR/PersonUpdateView.html'
    success_url = "/success/"

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

def getPersonList(request):
    return render(request,"HR/personInfo2Table.html")

def modPersonInfo(request, person_id):
    #查询编号对应的员工在页面显示进行人员编辑修改
    if person_id:
        p = Person.objects.get(pk=person_id)
        form = PersonForm(request.POST, instance=p)
    return render(request,'HR/addPersonInfo.html',{'form': form})
#new Person to Added
def addPersonInfo(request):
    if request.method=="POST":
        form = PersonForm(request.POST)
        #如果页面上面缺少和form对应的字段，is_valid()会失败，也没有提示。-_-||
        if form.is_valid():            
            # process the data in form.cleaned_data as required
            # p = addPersonForm(form.cleaned_data)
            # p.save()
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/success/")
        else:
            raise Http404 
    else:
        form = PersonForm()

    return render(request,'HR/addPersonInfo.html',{'form': form})

