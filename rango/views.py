from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category,Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list= Page.objects.order_by('-views')[:5]
    context_dict={'categories':category_list,'pages':page_list}
    return render(request, 'rango/index.html', context_dict)

def about(request):
     context_dict = {'boldmessage': "This is the about page"}
     return render(request, 'rango/about.html', context=context_dict)

def show_Category(request, category_name_url):
    context_dict={}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages']=pages
        context_dict['category']=category
    except Category.DoesNotExist:
        context_dict['pages']=None
        context_dict['category']=None

    return render(request, 'rango/category.html',context_dict)

def show_page(request, page_name_url):
    context_dict={}
    try:
        pages=Page.get(slug=page_name_slug)
        context_dict['pages']=pages
    except Page.DoesNotExist:
        context_dict['pages']=None

    return render(request,'rango/page.html',context_dict)
        

