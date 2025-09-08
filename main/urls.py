from django.urls import path
import main.views as views

app_name = 'main'

urlpatterns = [
    path('', views.show_index, name='index'),
]
