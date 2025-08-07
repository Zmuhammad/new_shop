from django.shortcuts import render , redirect
from django.views import View 
from .forms import UserRegisterationForm , VerifyCodeForm , UserLoginForm
from .models import User,OtpCode
from django.contrib import messages
import random
from utils import SendOtpCode
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UserRegisterationView (View):
    form_class = UserRegisterationForm

    def get (self , request):
        form = self.form_class
        return render (request , 'accounts/register.html' , {'form' : form})


    def post (self , request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000,9999)
            SendOtpCode(form.cleaned_data['phone_number'] , random_code)
            OtpCode.objects.create(phone_number = form.cleaned_data['phone_number'] , code = random_code) 

            request.session['user_registeration_info'] = {

                'phone_number' : form.cleaned_data['phone_number'],
                'email' : form.cleaned_data['email'],
                'full_name' : form.cleaned_data['full_name'],
                'password' : form.cleaned_data['password']  

            }

            messages.success (request , 'we sent you a Code' , 'success')
            return redirect ('account:verify_code')
        
        else:
            return render(request , 'accounts/register.html', {'form' : form})



class UserRegisterationVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get (self , request):
        form = self.form_class
        return render (request , 'accounts/verify.html' , {'form':form})

    def post(self, request):
        user_session = request.session['user_registeration_info']
        code_instance = OtpCode.objects.get(phone_number = user_session['phone_number'] )
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'],
                                         user_session['email'],
                                         user_session['full_name'],
                                         user_session['password'])
                
                code_instance.delete()
                messages.success(request , 'registeration success' , 'success')
                return redirect ('home:home')
            
            else :
                messages.error(request , 'registeration fail' , 'error')
                return redirect ('account:verify_code')
            
        return redirect ('home:home')
    

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get (self , request):
        form = self.form_class
        return render (request , self.template_name , {'form' : form})

    def post(self , request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number = cd['phone'] , password = cd['password'])
            if user is not None:
                login(request , user)
                messages.success (request , 'logging in successfully' , 'info')
                return redirect ('home:home')
            else:
                messages.error(request , 'phone number or password is wrong', 'info')
            
            return render (request , self.template_name , {'form' : form})
        

class UserLogoutView(LoginRequiredMixin , View):
    def get(self , request):
        logout(request)
        messages.success (request , 'logging out successfully' , 'info')
        return redirect('home:home')
    