from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect,Http404
from .models import Employee,Demission
from .forms import EmployeeForm,DemissionForm
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

class EmployeeListView(ListView):
    model = Employee
    ordering= ["-id"]
    context_object_name = 'Employee'
    template_name='HR/EmployeeListView.html'
    def get_queryset(self):
        #返回在职状态的人员
        return Employee.objects.filter(workStatus="00")
class EmployeeDetailView(DetailView):
    model = Employee
    template_name='EmployeeDetailView.html'

#通用编辑试图
class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name='HR/EmployeeCreateView.html'
    success_url = "/success/"
    
class EmployeeDeleteView(DeleteView):
    model = Employee
    context_object_name="Employee"
    template_name='HR/EmployeeConfirmDelete.html'
    success_url = "/success/"
    #我们必须在这里使用reverse_lazy()，而不是 reverse(),因为在导入文件时未加载URL
    # success_url = reverse_lazy('author-list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name='HR/EmployeeUpdateView.html'
    success_url = "/success/"

#办理离职
class DemissionCreateView(CreateView):
    model = Demission
    form_class = DemissionForm
    template_name='HR/DemissionCreateUpdateView.html'
    success_url = "/success/"
#更新离职数据
class DemissionUpdateView(UpdateView):
    model = Demission
    form_class = DemissionForm
    template_name='HR/DemissionCreateUpdateView.html'
    success_url = "/success/"
# Create your views here.
# 这是WebService接口返回Json格式
def getEmployeeinfo(request):
    #WebService接口，返回json格式数据 参考https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
    #动态获取列字段，和列字段对应的名字
    colMapping = {}
    for f in Employee._meta.fields:
        colMapping[f.name] = f.verbose_name
    l= list(colMapping.keys())
    # objs = Employee.objects.all().values(*l)
    #只显示在职人员
    objs = Employee.objects.filter(workStatus="00").values(*l)
    # print(colMapping)
    Employeelist = list(objs)

    return JsonResponse({"data":Employeelist}, safe=False)
    #return render(request,"HR/EmployeeInfo.html")

def getEmployeeList(request):
    return render(request,"HR/EmployeeInfo2Table.html")

def modEmployeeInfo(request, Employee_id):
    #查询编号对应的员工在页面显示进行人员编辑修改
    if Employee_id:
        p = Employee.objects.get(pk=Employee_id)
        form = EmployeeForm(request.POST, instance=p)
    return render(request,'HR/addEmployeeInfo.html',{'form': form})
#new Employee to Added
def addEmployeeInfo(request):
    if request.method=="POST":
        form = EmployeeForm(request.POST)
        #如果页面上面缺少和form对应的字段，is_valid()会失败，也没有提示。-_-||
        if form.is_valid():            
            # process the data in form.cleaned_data as required
            # p = addEmployeeForm(form.cleaned_data)
            # p.save()
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/success/")
        else:
            raise Http404 
    else:
        form = EmployeeForm()

    return render(request,'HR/addEmployeeInfo.html',{'form': form})

