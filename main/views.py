import re
import uuid
from django.shortcuts import render
from django.http import HttpResponseForbidden, FileResponse, HttpResponseServerError
from django.conf import settings

def show_index(request):
    context = {
        'npm': '2406404705',
        'name': 'Muhammad Fahri Muharram',
        'class': 'PBP E',
    }

    return render(request, 'index.html', context)

def show_static(request, name: str):
    # Matches /some-path/that-could/be-long/must-include/some-extension.txt-custom
    whitelist = r'^(?:[\w\-]+/)*[\w\-]+\.[\w\-]+$'
    if not re.match(whitelist, name):
        return HttpResponseForbidden(f'Static file name must match {whitelist}')
    path = f'{settings.STATIC_ROOT}/{name}'
    return FileResponse(open(path, 'rb'))

def show_product_list(request):
    return HttpResponseServerError()

def show_product_by_id(request, id: uuid.uuid4):
    return HttpResponseServerError()

def xml_product_list(request):
    return HttpResponseServerError()

def xml_product_by_id(request, id: uuid.uuid4):
    return HttpResponseServerError()

def json_product_list(request):
    return HttpResponseServerError()

def json_product_by_id(request, id: uuid.uuid4):
    return HttpResponseServerError()
