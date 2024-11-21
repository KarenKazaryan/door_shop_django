from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    return HttpResponse('<html><h1>Это большой текст заголовка</h1></html>')

def twink_page(request):
    return HttpResponse('Это вторая страница')
