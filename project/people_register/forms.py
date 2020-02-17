
from  .models import People
from django import forms
import re
from django.contrib.auth.models import User
# from django.core.validators import RegexValidator,MaxValueValidator, MinValueValidator
# name_valid = RegexValidator(r'[a-zA-Z ]+$', 'spaces before and after name is not allowed')
# pan_valid = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class PeopleForm(forms.ModelForm):

    class Meta:
        model= People
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super(PeopleForm,self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label='Select'
        self.fields['city'].empty_label=' '
   

    def clean_name(self):
            name = self.cleaned_data["name"]
            if not bool(re.search(r'[a-zA-Z ]+$',name)):
                raise forms.ValidationError("Please enter a valid name with no space before and after name ")
            else:
               return name
    
    def clean_pan_number(self):
            pan_number = self.cleaned_data["pan_number"]
            if not bool(re.search(r'^[0-9a-zA-Z]*$',pan_number)):
                raise forms.ValidationError("Please Enter Alphanumeric only")
            
            
            if User.objects.filter(username=self.cleaned_data['pan_number']).exists():
                raise forms.ValidationError("User With PAN No {pan_number} already exits")
            
            return pan_number
                
        

        


        





