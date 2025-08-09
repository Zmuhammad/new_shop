from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from .models import *
from .tasks import * 
from django.contrib import messages
from utils import *



# Create your views here.


class HomeView(View):
     def get(self , request , category_slug=None):
          categories = Category.objects.filter(is_sub =False)
          products = Product.objects.filter(available = True)

          if category_slug:
               category = Category.objects.get(slug = category_slug)
               products = Product.objects.filter(category = category)

          return render(request , 'home/home.html' , {'products' : products , 'categories': categories})
     

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
     

