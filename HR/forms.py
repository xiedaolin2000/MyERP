from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    def __init__(self, *args, **kwargs):        
        super(EmployeeForm, self).__init__(*args, **kwargs)        
        for field in iter(self.fields):            
            self.fields[field].widget.attrs.update({ 'class': 'form-control' })
    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['userName','']
    
    
    def __str__(self):
        return 