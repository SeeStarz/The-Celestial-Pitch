from django.urls import path
from django.conf import settings
import main.views as views

app_name = 'main'

urlpatterns = [
    path('', views.show_index, name='index'),
    path('product/', views.show_product_list, name='show_product_list'),
    path('product/<uuid:id>/', views.show_product_by_id, name='show_product_by_id'),
    path('xml/product', views.xml_product_list, name='xml_product_list'),
    path('xml/product/<uuid:id>/', views.xml_product_by_id, name='xml_product_by_id'),
    path('json/products', views.json_product_list, name='json_product_list'),
    path('json/product/<uuid:id>/', views.json_product_by_id, name='json_product_by_id'),
    # We remove prefix because for some reason django prepends slash and it breaks this
    path(settings.STATIC_URL.lstrip('/') + '<path:name>', views.show_static, name='static'),
]
