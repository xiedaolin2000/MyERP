from django.contrib import admin
from .models import Person,Performace,PerformaceDetail,Salary

# Register your models here.
admin.site.register(Person)
admin.site.register(Performace)
admin.site.register(PerformaceDetail)
admin.site.register(Salary)

