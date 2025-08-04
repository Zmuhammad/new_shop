from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreateForm (forms.ModelForm):
    password1 = forms.CharField(label = 'password' , widget=(forms.PasswordInput))
    password2 = forms.CharField(label = 'confirm password' , widget=(forms.PasswordInput))

    class Meta:
        model = User
        fields = ('email' , 'phone_number' , 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd ['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('passwords are NOT match')
        
        return cd['password2']
    
    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password (self.cleaned_data['password2'])
        if commit :
            user.save()

        else: 
            return user
        

class UserChangeForm (forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text = """you can change your password using 
                                         <a> href = \"../password/\" thisform</a>""")
    
    class Meta:
        model = User 
        fields = ('email' , 'phone_number' , 'full_name' , 'password' , 'last_login')


 
class UserRegisterationForm(forms.Form):
    phone_number = forms.CharField(max_length=11)
    full_name = forms.CharField (max_length=100)
    email = forms.EmailField()
    password = forms.CharField(label = 'password' , widget=(forms.PasswordInput))

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     user = user.objects.filter(email = email).exists()
    #     if user:
    #         raise ValidationError('this email already exists')
    #     return email
    

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data['phone_number']
    #     user = user.objects.filter(phone_number = phone_number).exists()
    #     if user:
    #         raise ValidationError('this phone_number already exists')
    #     return phone_number



class VerifyCodeForm ():
    code = forms.IntegerField()

                                

class UserLoginForm(forms.Form):
    phone = forms.CharField(max_length=11)
    password = forms.CharField(label = 'password' , widget=(forms.PasswordInput))