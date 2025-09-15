from django.urls import path
from django.conf import settings
import main.views as views

app_name = 'main'

urlpatterns = [
    path('', views.show_index, name='index'),
    # We remove prefix because for some reason django prepends slash and it breaks this
    path(settings.STATIC_URL.lstrip('/') + '<path:name>', views.show_static, name='static'),
]
