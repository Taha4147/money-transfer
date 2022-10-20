from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class myformModel(models.Model):
    name = models.CharField(max_length=150, blank=True)
    Email = models.EmailField(max_length=150, blank=True)
    phone = models.IntegerField(blank=True)
    website_name = models.CharField(max_length=150, blank=True)
    my_message = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class AddEmployeeModel(models.Model):
    user_id = models.TextField(null=True)
    user_name = models.CharField(max_length=150, null=True)
    Email = models.EmailField(max_length=150, null=True)
    phone = models.TextField(null=True)
    Address = models.CharField(max_length=150, null=True)
    Country = models.CharField(max_length=150, null=True)
    City = models.CharField(max_length=150, null=True)
    password = models.CharField(max_length=150, null=True)
    employee_pic = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.user_name

    @property
    def get_photo_url(self):
        if self.employee_pic and hasattr(self.employee_pic, 'url'):
            return self.employee_pic.url
        else:
            return "/static/images/upload-img.png"


class Expenses(models.Model):
    date = models.DateField(max_length=150, blank=True,)
    time = models.TimeField(max_length=150, blank=True)
    amount = models.TextField()
    used_for_purpose = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.used_for_purpose


class AddAgent(models.Model):
    user_id = models.TextField(null=True)
    user_name = models.CharField(max_length=150, null=True)
    Email = models.EmailField(max_length=150, null=True)
    phone = models.TextField(null=True)
    Country = models.CharField(max_length=150, null=True)
    City = models.CharField(max_length=150, null=True)
    password = models.CharField(max_length=150, null=True)
    employee_pic = models.ImageField(upload_to='images/', null=True)
    amount=models.IntegerField(null=True)
    def __str__(self):
        return self.user_name

    @property
    def get_photo_url(self):
        if self.agent_pic and hasattr(self.agent_pic, 'url'):
            return self.agent_pic.url
        else:
            return "/static/images/upload-img.png"


class Balance(models.Model):
    agent = models.ForeignKey(AddAgent, on_delete=models.CASCADE)
    date = models.DateField(max_length=150, blank=True)
    time = models.TimeField(max_length=150, blank=True)
    amount = models.IntegerField( blank=True)

    def __str__(self):
        return self.agent
