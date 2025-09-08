import re
from django.shortcuts import render
from django.http import HttpResponseForbidden, FileResponse

def show_index(request):
    context = {
        'npm': '2406404705',
        'name': 'Muhammad Fahri Muharram',
        'class': 'PBP E',
    }

    return render(request, 'index.html', context)

def show_static(request, name: str):
    whitelist = r'^[\w\-]+\.[\w\-]+$'
    if not re.match(whitelist, name):
        return HttpResponseForbidden(f'Static file name must match {whitelist}')
    return FileResponse(open(f'main/static/{name}', 'rb'))
