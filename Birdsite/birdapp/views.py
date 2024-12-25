from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Birds
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages


def index(request):
    birds=Birds.objects.all()
    paginator=Paginator(birds,6)
    page_number=request.GET.get('page')
    try:
        page_obj=paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj=paginator.page(1)
    except EmptyPage:
        page_obj=paginator.page(p.num_pages)

    return render(request,'index.html',dict(page_obj=page_obj))


def details(request,b_slug):
    birds=Birds.objects.get(slug=b_slug)
    return render(request,'details.html',dict(birds=birds))


def search(request):
    query=None
    bird=None
    if 'q'in request.GET:
        query=request.GET.get('q')
        bird=Birds.objects.all().filter(name__contains=query)
    return render(request,'search.html',dict(query=query,bird=bird))



