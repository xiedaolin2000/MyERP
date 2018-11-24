from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    def __init__(self, *args, **kwargs):        
        super(PersonForm, self).__init__(*args, **kwargs)        
        for field in iter(self.fields):            
            self.fields[field].widget.attrs.update({ 'class': 'form-control' })
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ['userName','']
    
    
    def __str__(self):
        return 