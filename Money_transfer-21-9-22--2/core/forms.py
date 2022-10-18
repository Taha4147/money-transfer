from django import forms
from django.utils.translation import gettext_lazy as _  
from .models import *
from core import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class addbalanceform(forms.ModelForm):
	class Meta:
		model = Balance
		fields = "__all__"
		
  
class CustomerRegistrationFrom(UserCreationForm):
    password1: forms.CharField(required=True,label='Password' ,widget=forms.PasswordInput(attrs={"autofocus": True,'class':'form-control'}))
    password2: forms.CharField(required=True,label='Confirm Password (again)' ,widget=forms.PasswordInput(attrs={"autofocus": True,'class':'form-control'}))
    email: forms.CharField(required=True ,widget=forms.EmailInput(attrs={"autofocus": True,'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels= {'email':'Email'}
        Widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-control'}),
    )

class AddEmployeeModelForm(forms.ModelForm):
    class Meta:
        model = models.AddEmployeeModel
        fields = "__all__"


class AddAgentForm(forms.ModelForm):
    class Meta:
        model = models.AddAgent
        fields = "__all__"
        
class ExpensesForm(forms.ModelForm):
    class Meta:
        model = models.Expenses
        fields = "__all__"