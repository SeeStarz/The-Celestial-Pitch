import re
import uuid
from datetime import datetime
from datetime import UTC
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponseForbidden, FileResponse, HttpResponseServerError, HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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

def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_product_list"))
            response.set_cookie('last_login', datetime.now(UTC).isoformat())
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.admin = request.user
        product_entry.save()
        return redirect('main:show_product_list')

    context = {'form': form}
    return render(request, 'create_product.html', context)

def show_product_list(request):
    product_list = Product.objects.all()

    last_login = request.COOKIES.get('last_login', None)
    if last_login:
        delta = datetime.now(UTC) - datetime.fromisoformat(last_login)
        second = int(delta.total_seconds())
        login_duration = second
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)
        login_duration = f'{hour:02}:{minute:02}:{second:02}'
    else:
        login_duration = None

    context = {
        'product_list': product_list,
        'login_duration': login_duration
    }

    return render(request, 'product_list.html', context)

def show_product_by_id(request, id: uuid.uuid4):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Http404()

    context = {
        'product': product
    }

    return render(request, 'product_detail.html', context)

@login_required(login_url='/login')
def checkout(request, id: uuid.uuid4):
    context = {}
    return render(request, 'checkout.html', context)

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
