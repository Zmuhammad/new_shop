from django.urls import path , include
from . import views

app_name= 'home'

# bucket_urls= [
#     path('' , views.BucketHome.as_view() , name='bucket'),
#     path('delete_bucket_obj/<str:key>/' , views.DeleteBucketObject.as_view() , name = 'delete_bucket_obj' ),
# ]

urlpatterns = [
    path('', views.HomeView.as_view() , name='home'),
    # path('bucket/', include(bucket_urls)),
    path('bucket' , views.BucketHome.as_view() , name='bucket'),
    path('delete_bucket_obj/<key>' , views.DeleteBucketObject.as_view() , name = 'delete_bucket_obj' ),    
    path('<slug:slug>/', views.ProductDetailView.as_view() , name='product_detail'),

]
