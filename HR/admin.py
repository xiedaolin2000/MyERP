from django.contrib import admin
from .models import Employee,Performace,PerformaceDetail,Salary

# Register your models here.
admin.site.register(Employee)
admin.site.register(Performace)
admin.site.register(PerformaceDetail)
admin.site.register(Salary)

