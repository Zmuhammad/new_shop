from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [

    path('register/' , views.UserRegisterationView.as_view() , name='user_register'),
    path('verify/' , views.UserRegisterationVerifyCodeView.as_view() , name = 'verify_code'),
    path('login/', views.UserLoginView.as_view() , name='login'),
    path('logout/', views.UserLogoutView.as_view() , name='logout'),
    
]