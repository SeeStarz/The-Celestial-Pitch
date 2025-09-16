import re
import uuid
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponseForbidden, FileResponse, HttpResponseServerError, HttpResponse, Http404
from django.conf import settings
from main.models import Product
from main.forms import ProductForm

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

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_product_list')

    context = {'form': form}
    return render(request, 'create_product.html', context)

def show_product_list(request):
    return HttpResponseServerError()

def show_product_by_id(request, id: uuid.uuid4):
    return HttpResponseServerError()

def xml_product_list(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize('xml', product_list)
    return HttpResponse(xml_data, content_type='application/xml')

def xml_product_by_id(request, id: uuid.uuid4):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Http404()
    xml_data = serializers.serialize('xml', [product])
    return HttpResponse(xml_data, content_type='application/xml')

def json_product_list(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize('json', product_list)
    return HttpResponse(json_data, content_type='application/json')

def json_product_by_id(request, id: uuid.uuid4):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Http404()
    json_data = serializers.serialize('json', [product])
    return HttpResponse(json_data, content_type='application/json')
