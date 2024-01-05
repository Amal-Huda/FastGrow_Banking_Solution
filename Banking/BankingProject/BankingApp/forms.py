from django import forms
from .import views
from .models import Customer,Districts,Branches
class Customerform(forms.ModelForm):
    Gender = forms.ChoiceField(choices=Customer.GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio-inline'}))
    Account_type = forms.MultipleChoiceField(choices=Customer.ACCOUNT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Materials = forms.MultipleChoiceField(choices=Customer.MATERIAL_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-inline'}))
    BirthDate=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model=Customer
        # fields=['name','dob','age','phone','address','account_type','materials','cust_district','cust_branch','gender']
        fields = ['Name','BirthDate','Gender','Age','Phone', 'Address', 'Account_type', 'Materials', 'District', 'Branch']
