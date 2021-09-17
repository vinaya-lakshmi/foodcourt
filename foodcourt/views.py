from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def home(request,c_slug=None):
    c_page=None
    prodt=None
    cat=None
    if c_slug!=None:
        c_page=get_object_or_404(categs,slug=c_slug)
        prodt=products1.objects.filter(category=c_page,available=True)
    else:
        cat=categs.objects.all()
        prodt=products1.objects.all().filter(available=True)

    paginator = Paginator(prodt,4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro= paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,"index.html",{'pr':prodt,'ct':cat,'pg':pro})

def prodDetails(request,c_slug,product_slug):
    try:
        prodt=products1.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,"item.html",{'pr':prodt})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products1.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,"search.html",{'qr':query,'pr':prod})
