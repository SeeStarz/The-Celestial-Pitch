import re
from django.shortcuts import render
from django.http import HttpResponseForbidden

def show_index(request):
    context = {
        'npm': '2406404705',
        'name': 'Muhammad Fahri Muharram',
        'class': 'PBP E',
    }

    return render(request, 'index.html', context)

def show_static(request, path: str):
    whitelist = r'^[\w\-]+\.[\w\-]+$'
    if not re.match(whitelist, path):
        return HttpResponseForbidden(f'Static path must match {whitelist}')

    return render(request, f'static/{path}', context)
