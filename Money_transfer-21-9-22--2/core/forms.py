from django import forms
from django.utils.translation import gettext_lazy as _  
from .models import *
from core import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class DateInput(forms.DateInput):
    input_type = 'date'

class addbalanceform(forms.ModelForm):
	class Meta:
		model = Balance
		fields = "__all__"
		
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput())
	id2 = forms.CharField(label='id',widget=forms.TextInput())
	phone = forms.CharField(label='phone',widget=forms.TextInput())
	type = forms.CharField(label='type', widget=forms.TextInput())    
	amount = forms.CharField(label='amount',widget=forms.TextInput())    
	country = forms.CharField(label='country', widget=forms.TextInput())    
	city = forms.CharField(label='city', widget=forms.TextInput())  
	# creater = forms.CharField(label='creater', widget=forms.TextInput())  
	image = forms.ImageField(label='image',)  
	class Meta:
		model = get_user_model()
		fields = ("id2","username", "email", "password1", "password2","phone","amount","country","city","type","image")
  

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


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = models.Expenses
        fields = "__all__"