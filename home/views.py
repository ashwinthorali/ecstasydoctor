from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'index.html', context)

def contact(request):
    context = {

    }
    return render(request, 'contact.html', context)


def mca(request):
    context = {

    }
    return render(request, 'mca.html', context)

def ccp(request):
    context = {

    }
    return render(request, 'ccp.html', context)


def industry(request):
    data = Industry.objects.all().order_by('id')
    context = {
        'data':data,
    }
    return render(request, 'industry.html', context)

def apply(request):
    context = {

    }
    return render(request, 'apply.html', context)




def blogs(request):
    data1 = Blog.objects.filter(status=True).order_by('id')
    page = request.GET.get('page', 1)

    
    paginator = Paginator(data1, 6)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {
        'data':data,
    }
    return render(request, 'blogs.html', context)


def blogs_detail(request, pk):
    data = Blog.objects.get(slug=pk)
    context = {
        'data':data,
    }
    return render(request, 'blogs_detail.html', context)

#new changes

def careers(request):
    data = Careers.objects.all().order_by('-id')
    context = {
        'data':data,
    }
    return render(request, 'career.html', context)



def referral(request):
    context = {
    }
    return render(request, 'referral.html', context)


def referral_td(request):
    data = Referral_terms_and_condition.objects.last()
    context = {
        'data':data,
    }
    return render(request, 'terms-and-condition.html', context)    

def term(request):
    data = Terms_and_condition.objects.last()
    context = {
        'data':data,
    }
    return render(request, 'term.html', context)    


def privacy(request):
    data = Terms_and_condition.objects.last()
    context = {
        'data':data,
    }
    return render(request, 'privacy.html', context)    




def careers_detail(request, pk):
    data = Careers.objects.get(id=pk)
    context = {
        'data':data,
    }
    return render(request, 'careers_detail.html', context)
