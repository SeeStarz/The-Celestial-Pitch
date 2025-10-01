from django.urls import path
from django.conf import settings
import main.views as views

app_name = 'main'

urlpatterns = [
    path('', views.show_index, name='index'),
    path('product/form/', views.create_product, name='create_product'),
    path('product/', views.show_product_list, name='show_product_list'),
    path('product/<uuid:id>/', views.show_product_by_id, name='show_product_by_id'),
    path('xml/product/', views.xml_product_list, name='xml_product_list'),
    path('xml/product/<uuid:id>/', views.xml_product_by_id, name='xml_product_by_id'),
    path('json/product/', views.json_product_list, name='json_product_list'),
    path('json/product/<uuid:id>/', views.json_product_by_id, name='json_product_by_id'),
    path('checkout/<uuid:id>/', views.checkout, name='checkout'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
