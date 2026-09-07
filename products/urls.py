from django.urls import path , include
from . import views

app_name = 'product'

urlpatterns = [
    path('single_product' , views.single , name= 'single' ),
    path('category/' , views.category , name = 'category')
]
