from django.contrib import admin

from core.views import Balance
from .models import  AddEmployeeModel, Expenses, Balance, AddAgent
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

admin.site.register(AddEmployeeModel)
admin.site.register(Expenses)
admin.site.register(Balance)
admin.site.register(AddAgent)
