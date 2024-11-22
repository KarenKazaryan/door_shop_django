from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    return HttpResponse('<html><h1>Это большой текст заголовка</h1></html>')


