from django.shortcuts import render
from .models import *

def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss':newss})
