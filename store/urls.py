from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home, name='api_home'),
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
    path('categories/', views.category_list),
    path('orders/', views.create_order),
    path('register/', views.register_user),
    path('login/', views.login_user),
    path('newsletter/', views.subscribe_newsletter),
    
]