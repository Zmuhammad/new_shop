from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [

    path('register/' , views.UserRegisterationView.as_view() , name='user_register'),
    path('verify/' , views.UserRegisterationVerifyCodeView.as_view() , name = 'verify_code'),
    
]