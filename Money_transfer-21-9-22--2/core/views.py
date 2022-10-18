from django.views import View
from django.shortcuts import render, redirect
from .models import AddAgent, Balance, Expenses, AddEmployeeModel
from django.contrib import messages
from .forms import addbalanceform
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from core import forms
from django.contrib.auth import login, authenticate, logout 
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
        print(form.errors)
        context['form']=form
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
        form=forms.AddEmployeeModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request=request,template_name=self.template)
    
class  add_agent_view(View):
    template='add-new-agent.html'
    context={}
    def get(self,request):
        return render(request=request, template_name=self.template) 
    def post(self,request):
        form=forms.AddAgentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        print(form.errors)
        return render(request=request,template_name=self.template)


class agent_list(View):
    tempalate='agents.html'
    context={}
    def get(self,request):
        context=self.context
        context['queryset']=AddAgent.objects.all()
        return render (request=request ,template_name=self.tempalate, context=self.context)
    
    
class employee_details(View):
    tempalate='employee.html'
    context={}
    def get(self,request):
        context=self.context
        context['queryset']= AddEmployeeModel.objects.all()
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


def add_balance(request):
    print("------------balance-------------")
    
    agent_list = AddAgent.objects.all()

    context = {'agent_list': agent_list}

    if request.method == 'POST':
        amount = request.POST['amount']
        print(amount)
        name = request.POST['agent']
        print(name)
        get_name = forms.AddAgent.objects.get(user_name__icontains=name)
        get_name.amount = (get_name.amount + int(amount))
        get_name.save()
        print("save")
        form = forms.addbalanceform(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        print(form.errors)
        return redirect("Balance_details")

    return render(request, 'add-balance.html', context)


def Balance_details(request):

    queryset = Balance.objects.all()
    print(queryset)
    context = {

        'queryset': queryset
    }
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     Email = request.POST['Email']
    #     phone = request.POST['phone']
    #     website_name = request.POST['website_name']
    #     my_message = request.POST['my_message']
    #     new_record = myformModel(
    #         name=name, Email=Email, phone=phone, website_name=website_name, my_message=my_message)
    #     new_record.save()
    return render(request, 'balance-history.html', context)


class payroll(View):
    template='payroll.html'
    context={}
    def get(self,request):
        context=self.context
        context['queryset']= AddAgent.objects.all()
        return render(request=request, template_name=self.template , context=self.context)

    def post(self,request):
        context=self.context
        context['check_list'] = request.POST.getlist('check')
        context['amount'] = request.POST.getlist('amount')
        for i in context['check_list']:
            print(i)
            payroll = AddAgent.objects.get(id=i)
            for j in context['amount']:
                if j != "":
                    print("1")
                    payroll.amount = (payroll.amount + int(j))
                    payroll.save()
                    break
        return render(request=request, template_name=self.template , context=self.context)
 