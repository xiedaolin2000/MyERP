from django.forms import ModelForm
from .models import Organization

class OrganizationForm(ModelForm):
    def __init__(self, *args, **kwargs):        
        super(OrganizationForm, self).__init__(*args, **kwargs)
        #使用bootstrap模板
        for field in iter(self.fields):            
            self.fields[field].widget.attrs.update({ 'class': 'form-control' })
    class Meta:
        model = Organization
        fields = '__all__'