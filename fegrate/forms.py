from django import forms
from .models import *
from crispy_forms.helper import FormHelper

class PostForm(forms.ModelForm) :
    class Meta:
        model = Post
        fileds = ('Title','Content')
        exclude = ['username','created_at']


class FCLForm(forms.ModelForm) :
    
    class Meta:
        model = FCL
        fields = ('chk_date','origin','dest','carrier','twenty','fourty','freq','ttime','effective','scno','remark',)
        exclude = ['username']
        widgets = {
        'chk_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
        'effective': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
        
        }


        
        
    def __init__(self, *args, **kwargs):
        super(FCLForm,self).__init__(*args, **kwargs)

        self.fields['chk_date'].required = False  #필수 입력값 아님
        self.fields['origin'].required = False
        self.fields['dest'].required = False
        self.fields['carrier'].required = False
        self.fields['twenty'].required = False
        self.fields['fourty'].required = False
        self.fields['freq'].required = False
        self.fields['ttime'].required = False
        self.fields['effective'].required = False
        self.fields['scno'].required = False
        self.fields['remark'].required = False
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        
class AirfreightForm(forms.ModelForm) :
    
    class Meta:
        model = Airfreight
        fields = '__all__'
        exclude = ['username']
        # labels = {
        # }
        widgets = {
        'air_chk_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
        'air_effective': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
        
        }
        
        
    def __init__(self, *args, **kwargs):
        super(AirfreightForm,self).__init__(*args, **kwargs)

        self.fields['air_consol'].required = False  #필수 입력값 아님
        self.fields['air_chk_date'].required = False
        self.fields['air_origin'].required = False
        self.fields['air_dest'].required = False
        self.fields['air_carrier'].required = False
        self.fields['air_min'].required = False
        self.fields['air_normal'].required = False
        self.fields['air_45kg'].required = False
        self.fields['air_100kg'].required = False
        self.fields['air_300kg'].required = False
        self.fields['air_500kg'].required = False
        self.fields['air_1000kg'].required = False
        self.fields['air_fsc'].required = False
        self.fields['air_iss'].required = False
        self.fields['air_tspoint'].required = False
        self.fields['air_skdl'].required = False
        self.fields['air_remark'].required = False
        self.fields['air_effective'].required = False
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        
        
class LCLForm(forms.ModelForm) :
    
    class Meta:
        model = LCL
        fields = ('LCL_chk_date','LCL_origin','LCL_dest','LCL_ofc','LCL_consol','LCL_ttime','LCL_effective','LCL_remark','LCL_ofcunit')
        exclude = ['username']

        # labels = {
            
        # }
        widgets = {
        'LCL_chk_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
        'LCL_effective': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
        
        }
        
        
        
    def __init__(self, *args, **kwargs):
        super(LCLForm,self).__init__(*args, **kwargs)

        self.fields['LCL_chk_date'].required = False  #필수 입력값 아님
        self.fields['LCL_origin'].required = False
        self.fields['LCL_dest'].required = False
        self.fields['LCL_ofc'].required = False
        self.fields['LCL_consol'].required = False
        self.fields['LCL_ttime'].required = False
        self.fields['LCL_effective'].required = False
        self.fields['LCL_remark'].required = False
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        
        
class Local_AirForm(forms.ModelForm):
    class Meta:
        model = Local_Air
        fields = '__all__'
        exclude = ['username']
        
    def __init__(self, *args, **kwargs):
        super(Local_AirForm,self).__init__(*args, **kwargs)

        self.fields['Loc_Air_Hdc'].required = False 
        self.fields['Loc_Air_Hdcunit'].required = False
        self.fields['Loc_Air_Clc'].required = False 
        self.fields['Loc_Air_Clcunit'].required = False
        self.fields['Loc_Air_Doc'].required = False 
        self.fields['Loc_Air_Docunit'].required = False
        self.fields['Loc_Air_Thc'].required = False 
        self.fields['Loc_Air_Thcunit'].required = False
        self.fields['Loc_Air_Otc'].required = False
        self.fields['Loc_Air_Remark'].required = False
        
        self.helper = FormHelper()
        self.helper.form_show_labels = False     
        
class Local_LclForm(forms.ModelForm):
    class Meta:
        model = Local_Lcl
        fields = '__all__'
        exclude = ['username']
        
    def __init__(self, *args, **kwargs):
        super(Local_LclForm,self).__init__(*args, **kwargs)
        
        self.fields['Loc_Lcl_Cfs'].required = False 
        self.fields['Loc_Lcl_Cfsunit'].required = False
        self.fields['Loc_Lcl_Doc'].required = False 
        self.fields['Loc_Lcl_Docunit'].required = False
        self.fields['Loc_Lcl_Hdc'].required = False 
        self.fields['Loc_Lcl_Hdcunit'].required = False
        self.fields['Loc_Lcl_Clc'].required = False 
        self.fields['Loc_Lcl_Clcunit'].required = False
        self.fields['Loc_Lcl_Blf'].required = False 
        self.fields['Loc_Lcl_Blfunit'].required = False
        self.fields['Loc_Lcl_Otc'].required = False
        self.fields['Loc_Lcl_Remark'].required = False
        
        self.helper = FormHelper()
        self.helper.form_show_labels = False     
        
class Local_FclForm(forms.ModelForm):
    class Meta:
        model = Local_Fcl
        fields = '__all__'
        exclude = ['username']
        
    def __init__(self, *args, **kwargs):
        super(Local_FclForm,self).__init__(*args, **kwargs)
        
        self.fields['Loc_Fcl_Thc'].required = False 
        self.fields['Loc_Fcl_Doc'].required = False
        self.fields['Loc_Fcl_Vgm'].required = False 
        self.fields['Loc_Fcl_Seal'].required = False
        self.fields['Loc_Fcl_Clc'].required = False 
        self.fields['Loc_Fcl_Hdc'].required = False
        self.fields['Loc_Fcl_Otc'].required = False 
        self.fields['Loc_Fcl_Remark'].required = False
        self.helper = FormHelper()
        self.helper.form_show_labels = False   
        
class Dest_AirForm(forms.ModelForm):
    class Meta:
        model = Dest_Air
        fields = '__all__'
        exclude = ['username']
        
    def __init__(self, *args, **kwargs):
        super(Dest_AirForm,self).__init__(*args, **kwargs)

        self.fields['Dest_Air_Hdc'].required = False 
        self.fields['Dest_Air_Hdcunit'].required = False
        self.fields['Dest_Air_Clc'].required = False 
        self.fields['Dest_Air_Clcunit'].required = False
        self.fields['Dest_Air_Doc'].required = False 
        self.fields['Dest_Air_Docunit'].required = False
        self.fields['Dest_Air_Thc'].required = False 
        self.fields['Dest_Air_Thcunit'].required = False
        self.fields['Dest_Air_Otc'].required = False
        self.fields['Dest_Air_Remark'].required = False
        
        self.helper = FormHelper()
        self.helper.form_show_labels = False    
        
class Dest_LclForm(forms.ModelForm):
    class Meta:
        model = Dest_Lcl
        fields = '__all__'
        exclude = ['username']
        
    def __init__(self, *args, **kwargs):
        super(Dest_LclForm,self).__init__(*args, **kwargs)
        
        self.fields['Dest_Lcl_Baf'].required = False 
        self.fields['Dest_Lcl_Bafunit'].required = False
        self.fields['Dest_Lcl_Caf'].required = False 
        self.fields['Dest_Lcl_Cafunit'].required = False
        self.fields['Dest_Lcl_Drc'].required = False 
        self.fields['Dest_Lcl_Drcunit'].required = False
        self.fields['Dest_Lcl_Ccc'].required = False 
        self.fields['Dest_Lcl_Cccunit'].required = False
        self.fields['Dest_Lcl_Thc'].required = False 
        self.fields['Dest_Lcl_Thcunit'].required = False
        self.fields['Dest_Lcl_Doc'].required = False
        self.fields['Dest_Lcl_Hdc'].required = False 
        self.fields['Dest_Lcl_Clc'].required = False 
        self.fields['Dest_Lcl_Whc'].required = False 
        self.fields['Dest_Lcl_Whc'].required = False 
        self.fields['Dest_Lcl_Otc'].required = False
        self.fields['Dest_Lcl_Remark'].required = False
        
        self.helper = FormHelper()
        self.helper.form_show_labels = False  
        
class Dest_FclForm(forms.ModelForm):
    class Meta:
        model = Dest_Fcl
        fields = '__all__'
        exclude = ['username']
        
    def __init__(self, *args, **kwargs):
        super(Dest_FclForm,self).__init__(*args, **kwargs)
        
        self.fields['Dest_Fcl_Thc'].required = False 
        self.fields['Dest_Fcl_Doc'].required = False
        self.fields['Dest_Fcl_Wfc'].required = False 
        self.fields['Dest_Fcl_Ccc'].required = False
        self.fields['Dest_Fcl_Cic'].required = False 
        self.fields['Dest_Fcl_Hdc'].required = False
        self.fields['Dest_Fcl_Otc'].required = False 
        self.fields['Dest_Fcl_Remark'].required = False
        self.helper = FormHelper()
        self.helper.form_show_labels = False  