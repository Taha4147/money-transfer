from django.views import View
from django.shortcuts import render, redirect
from .models import  Balance, Expenses,User
from django.contrib import messages
# from django.contrib.auth.models import User
from core import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.

class dashboard(View):
    template= 'dashboard.html'
    context={}
    def get(self,request):
        context=self.context
        return render(request=request,template_name= self.template, context=self.context)

class register(View):
    template= 'register.html'
    context={}
    def get(self,request):
        return render(request=request, template_name=self.template, context=self.context)
    def post(self,request):
        context=self.context
        form = forms.CustomerRegistrationFrom(request.POST)
        if form.is_valid():
            messages.success(request , "congratulations!! Registered Sucessfully")
            form.save()
        password1 = form.data['password1']
        password2 = form.data['password2']
        email = form.data['email']
        for msg in form.errors.as_data():
            if msg == 'email':
                messages.error(request, f"Declared {email} is not valid")
            if msg == 'password2' and password1 == password2:
                messages.error(request, f"Selected Password is not strong enough")
            elif msg == 'password2' and password1 != password2:
                messages.error(request, f"Password do not match")
        return render(request=request, template_name=self.template, context=self.context)
    

class user_login(View):
    template='user-login.html'
    context={}
    def get(self,request):
        return render(request=request, template_name=self.template)
    
    def post(self,request):
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active == True:
                    login(request,user)
                    if request.user.is_superuser:
                        messages.success(request, "You are successfully login")	
                        return redirect("/dashboard")
                    else:
                        messages.success(request, "You are successfully login")	
                        return redirect("/dashboard")
                else:
                    messages.error(request,"Your account is not active.")
        else:
            if User.objects.filter(username=request.POST['username']).exists():
                messages.error(request,"Invalid password.")
            else:
                messages.error(request,"Invalid username.")
        context = self.context
        context["login_form"] = form
        return render(request=request, template_name=self.template, context=context)
    
    
class  add_employee_view(View):
    template='add-new-employee.html'
    context={}
    def get(self,request):
        return render(request=request, template_name=self.template) 
    def post(self,request):
        form=forms.NewUserForm(request.POST, request.FILES)
        print(request.POST)
        # print(request.FILES)
        if form.is_valid():
            form.save()
        print(form.errors)
        return render(request=request,template_name=self.template)
    
class  add_agent_view(View):
    template='add-new-agent.html'
    context={}
    def get(self,request):
        return render(request=request, template_name=self.template) 
    def post(self,request):
        form=forms.NewUserForm(request.POST, request.FILES)
        print("request POST is: ",request.POST)
        if form.is_valid():
            form.save()
        print(form.errors)
        return render(request=request,template_name=self.template)


class agent_list(View):
    tempalate='agents.html'
    context={}
    def get(self,request):
        context=self.context
        print("user is",request.user)
        context['queryset']=User.objects.filter(type='agent')
        return render (request=request ,template_name=self.tempalate, context=self.context)
    
    
class employee_details(View):
    tempalate='employee.html'
    context={}
    def get(self,request):
        context=self.context
        # context['queryset']= AddEmployeeModel.objects.all()
        return render (request=request ,template_name=self.tempalate, context=self.context)


class expenses(View):
    template= 'expenses.html'
    context={}
    def get(self,request):
        context=self.context
        context['queryset']=Expenses.objects.all()
        return render(request=request, template_name=self.template,context=self.context)
    def post(self,request):
        context=self.context
        form=forms.ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
        context['queryset']=Expenses.objects.all()
        return render(request=request, template_name=self.template,context=self.context)


class add_balance(View):
    template= 'add-balance.html'
    context={}
    def get(self,request):
        context=self.context
        # context['agent_list']=AddAgent.objects.all()
        return render(request=request,template_name=self.template,context=self.context)
    def post(self,request):
        amount = request.POST['amount']
        name = request.POST['agent']
        get_name = forms.AddAgent.objects.get(pk=name)
        get_name.amount = (get_name.amount + int(amount))
        get_name.save()
        form = forms.addbalanceform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("Balance_details")

class Balance_details(View):
    template='balance-history.html'
    context={}
    def get(self,request):
        context=self.context
        context['queryset']=Balance.objects.all()
        return render(request=request,template_name=self.template,context=self.context)
    


class payroll(View):
    template='payroll.html'
    context={}
    def get(self,request):
        context=self.context
        # context['queryset']= AddAgent.objects.all()
        return render(request=request, template_name=self.template , context=self.context)

    def post(self,request):
        context=self.context
        context['check_list'] = request.POST.getlist('check')
        context['amount'] = request.POST.getlist('amount')
        for i in context['check_list']:
            print(i)
            # payroll = AddAgent.objects.get(id=i)
            for j in context['amount']:
                if j != "":
                    payroll.amount = (payroll.amount + int(j))
                    payroll.save()
                    context['payroll']=payroll
                    break
        return render(request=request, template_name=self.template , context=self.context)

class orders(View):
    template='orders-1.html'
    context={}
    def get(self,request):
        context=self.context
        return render(request=request, template_name=self.template, context=self.context)

class add_new_order(View):
    template='add-new-order.html'
    context={}
    def get(self,request):
        context=self.context
        return render(request=request, template_name=self.template, context=self.context)


class new_orders(View):
    template='add-new-order-9.html'
    context={}
    def get(self,request):
        context=self.context
        return render(request=request, template_name=self.template, context=self.context)


class canceled_orders(View):
    template='can-order.html'
    context={}
    def get(self,request):
        context=self.context
        return render(request=request, template_name=self.template, context=self.context)

class payment_sucessfully(View):
    template='payment_sucecessfull.html'
    context={}
    def get(self,request):
        context=self.context
        return render(request=request, template_name=self.template, context=self.context)