import re
import os
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
    with open('log.txt', 'a') as file:
        file.write(f'Trying to process {name}\n')
    # Matches /some-path/that-could/be-long/must-include/some-extension.txt-custom
    whitelist = r'^(?:[\w\-]+/)*[\w\-]+\.[\w\-]+$'
    if not re.match(whitelist, name):
        return HttpResponseForbidden(f'Static file name must match {whitelist}')
    path = f'{os.getenv("STATIC_ROOT")}/{name}'
    with open('log.txt', 'a') as file:
        file.write(f'Trying to serve {path}\n')
    return FileResponse(open(path, 'rb'))
