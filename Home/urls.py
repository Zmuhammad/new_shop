from django.urls import path , include
from . import views

app_name= 'home'

bucket_urls= [
    path('' , views.BucketHome.as_view() , name='bucket'),
    path('delete_bucket_obj/<str:key>/' , views.DeleteBucketObject.as_view() , name = 'delete_bucket_obj' ),
    path('download_bucket_obj/<str:key>/' , views.DownloadBucketObject.as_view() , name = 'download_bucket_obj' ),
]

urlpatterns = [
    path('', views.HomeView.as_view() , name='home'),
    path('detail/<slug:slug>/', views.ProductDetailView.as_view() , name='product_detail'),
    path('category/<slug:category_slug>/', views.HomeView.as_view() ,name='category_filter'),
    path('bucket/', include(bucket_urls)),  
     
    

]