from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from .models import Product
from .tasks import * 
from django.contrib import messages
from utils import *


# all_bucket_objects_task , delete_object_task , download_object_task


# Create your views here.


class HomeView(View):
     def get(self , request):
          products = Product.objects.filter(available = True)
          return render(request , 'home/home.html' , {'products' : products})
     

class ProductDetailView(View):
     def get (self , request , slug):
          product = get_object_or_404(Product, slug = slug)
          return render(request , 'home/detail.html' , {'product':product})
     

class BucketHome (IsAdminUserMixin , View):
     template_name = 'home/bucket.html'

     def get (self , request):
          objects = all_bucket_objects_task()
          print('-' * 100)
          print(objects)
          return render (request , self.template_name ,{'objects':objects})
     

     
class DeleteBucketObject(IsAdminUserMixin , View):
     def get (self , request , key):
          delete_object_task.delay(key)
          messages.success(request , 'object will delete shortly' , 'info')
          return redirect('home:bucket')
     


class DownloadBucketObject(IsAdminUserMixin , View):
     def get (self , request , key):
          download_object_task.delay(key)
          messages.success(request , 'object will download shortly' , 'info')
          return redirect('home:bucket') 
     

