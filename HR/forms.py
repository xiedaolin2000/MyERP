from django.forms import ModelForm
from .models import Employee,Performace, Demission
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class EmployeeForm(ModelForm):
    def __init__(self, *args, **kwargs):        
        super(EmployeeForm, self).__init__(*args, **kwargs)
        #改用crispy_forms tag
        # for field in iter(self.fields):            
        #     self.fields[field].widget.attrs.update({ 'class': 'form-control' })
        self.helper = FormHelper()
        self.helper.form_method="post"
        self.helper.form_tag = False
        self.helper.form_action="{% url 'Employee-add' %}"
        self.helper.add_input(Submit("submit","Save"))
    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['userName','']
    
    
    def __str__(self):
        return

class PerformaceForm(ModelForm):
    def __init__(self, *args, **kwargs):        
        super(PerformaceForm, self).__init__(*args, **kwargs)        
        for field in iter(self.fields):            
            self.fields[field].widget.attrs.update({ 'class': 'form-control' })
    class Meta:
        model = Performace
        fields = '__all__'    
    
    def __str__(self):
        return

class DemissionForm(ModelForm):
    def __init__(self, *args, **kwargs):        
        super(DemissionForm, self).__init__(*args, **kwargs)        
        for field in iter(self.fields):            
            self.fields[field].widget.attrs.update({ 'class': 'form-control' })
    class Meta:
        model = Demission
        fields = '__all__'    
    
    def __str__(self):
        return ""