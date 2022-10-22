from django.contrib import admin
from core import models
from core.views import Balance
from .models import   Expenses, Balance
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


#User Table
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username","type" ,"email","phone","amount","country","city"]
    
admin.site.register(Expenses)
admin.site.register(Balance)
