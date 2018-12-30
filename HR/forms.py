from django.forms import ModelForm
from .models import Employee,Performace, Demission,BackBone
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Fieldset,Div,Column,Row,Field

class EmployeeForm(ModelForm):
    def __init__(self, *args, **kwargs):        
        super(EmployeeForm, self).__init__(*args, **kwargs)
        #改用crispy_forms tag
        # for field in iter(self.fields):            
        #     self.fields[field].widget.attrs.update({ 'class': 'form-control' })
        self.helper = FormHelper()
        self.helper.form_method="POST"
        # self.helper.form_action="{% url 'Employee-add' %}"
        # self.helper.form_action="Employee-add"
        self.helper.layout = Layout(
            Fieldset(
                "人员基本信息",
                Row(                    
                    Column("userName"   , css_class="col-sm-4"),
                    Column("workNo"     , css_class="col-sm-4"),
                    Column("IDNo"       , css_class="col-sm-4")                                     
                    ),
                Row(
                    Column("sex"        ,   css_class="col-sm-4"),
                    Column("entryDate"  ,   css_class="col-sm-4"),
                    Column("maritalStatus", css_class="col-sm-4")   
                ),
                Row(
                    Column("mobilePhone", css_class="col-sm-4"),
                    Column("email"     ,  css_class="col-sm-4"),                   
                    Column("email2"      , css_class="col-sm-4")
                    ),
                Row(
                    
                    Column("birthDay",      css_class="col-sm-4"),
                    Column("provinceBirth", css_class="col-sm-4"),
                    Column("cityBirth", css_class="col-sm-4")
                    ),
                Row(
                    Column("workNoExt"     , css_class="col-sm-4"),                    
                    Column("emergencyReleation", css_class="col-sm-4"),
                    Column("emergencyContact", css_class="col-sm-4")
                    ),
                Row(
                    Column("address", css_class="col-sm-12")
                    )
            ),
            Fieldset(
                "项目信息",
                Row(
                    Column("role"          , css_class="col-sm-4"),
                    Column("level"          , css_class="col-sm-4"),
                    Column("majorSkill"     , css_class="col-sm-4")
                    ),
                Row(                    
                    Column("depart"    ,    css_class="col-sm-4"),
                    Column("projectName",   css_class="col-sm-4")
                    ),
            ),
            Fieldset(
                "毕业学校",
                Row(
                    Column("graduatedSchool",   css_class="col-sm-4"),
                    Column("profession",        css_class="col-sm-4"),
                    Column("schoolType",        css_class="col-sm-4")
                ),
                Row(
                    
                    Column("education",         css_class="col-sm-4"),
                    Column("graduatedDay",      css_class="col-sm-4"),
                ),
            ),
            "user",
            "headPicPath"

        )
        self.helper.add_input(Submit("submit","保存"))

    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['userName','']    
    def __str__(self):
        return


        
            

class BackBoneForm(ModelForm):
    def __init__(self, *args, **kwargs):        
        super(BackBoneForm, self).__init__(*args, **kwargs)
        #改用crispy_forms tag
        # for field in iter(self.fields):            
        #     self.fields[field].widget.attrs.update({ 'class': 'form-control' })
        self.helper = FormHelper()
        self.helper.form_method="post"
        self.helper.form_tag = False
        self.helper.form_action= reverse_lazy("BackBone-add")
        self.helper.add_input(Submit("submit","保存"))
    class Meta:
        model = BackBone
        fields = '__all__'        
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