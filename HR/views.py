from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect,Http404
from .models import Employee,Demission, BackBone
from .forms import EmployeeForm,DemissionForm,BackBoneForm
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

class EmployeeListView(LoginRequiredMixin,ListView):
    model = Employee
    ordering= ["-id"]
    context_object_name = 'Employee'
    template_name='HR/EmployeeListView.html'
    def get_queryset(self):
        #返回在职状态的人员
        return Employee.objects.filter(workStatus="00")

class QueryResultListView(ListView):
    model = Employee
    ordering= ["-id"]
    context_object_name = 'Employee'
    template_name='HR/QueryResultListView.html'
    def get_queryset(self):
        #
        queryValue = self.request.GET["q"].upper()
        if queryValue.isdecimal() or queryValue.startswith("B-"):
            qs = Employee.objects.filter( workNo__contains   = queryValue,  workStatus="00")
        else:
            qs = Employee.objects.filter( userName__contains = queryValue,  workStatus="00")
        #返回符合查询条件的在职状态人员
        return qs

class EmployeeDetailView(LoginRequiredMixin,DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name='HR/EmployeeDetailView.html'

#通用编辑试图
class EmployeeCreateView(CreateView): 
    model = Employee
    form_class = EmployeeForm    
    template_name='HR/EmployeeCUDView.html'
    #我们必须在这里使用 reverse_lazy()，而不是 reverse(),因为在导入文件时未加载URL
    success_url = reverse_lazy('success')
    def get_form(self):
        f = super().get_form()
        f.helper.form_action="Employee-add"
        return f
    
class EmployeeDeleteView(DeleteView):
    model = Employee
    context_object_name="Employee"
    template_name='HR/EmployeeConfirmDelete.html'
    #我们必须在这里使用 reverse_lazy()，而不是 reverse(),因为在导入文件时未加载URL
    success_url = reverse_lazy('success')
    
    # success_url = reverse_lazy('author-list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name='HR/EmployeeCUDView.html'
    #我们必须在这里使用 reverse_lazy()，而不是 reverse(),因为在导入文件时未加载URL
    success_url = reverse_lazy('success')

    def get_form(self):
        f = super().get_form()
        f.helper.form_action=reverse("Employee-update", args=[self.object.user.id])
        return f

class BackBoneCreateView(CreateView):
    model = BackBone
    form_class = BackBoneForm
    template_name='HR/BackBoneUpdateView.html'
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

from django.db.models import Count
def dashboard_HR(request):
    para1 = request.GET.get("q")
    print("url parameter is %s" %(para1))
    #如果在分组统计的聚合函数的时候，如果模型设置了META.ordering，一定要用order_by()否则结果无法预料
    sex_ratio = Employee.objects.values("sex").annotate(Count("user")).order_by()
    #获取模型中的下拉列表选项,是元组列表
    t = Employee._meta.get_field('sex').choices
    d = dict(t)
    #把分组记录集中的编码转换为对应的显示名称，为什么在后台转换，而不在前台转换，是保持代码统一性 DRY（Don't Repeat Yourself），这样只要在models修改一次就可以
    for s in sex_ratio:
        s["sex"]=d[s["sex"]]
    
    #统计项目组人数,多表关联查询 范例
    prj_ratio=Employee.objects.values("depart__nodeName").annotate(Count("user")).order_by()
    return render(request,template_name="HR/HR_DashBoard.html", context={ "sex_ratio":sex_ratio, "prj_ratio":prj_ratio} )

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

