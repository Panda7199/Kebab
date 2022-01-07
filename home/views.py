from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from blog.models import Blog
from home.forms import ContactForm, Comment_detail_Form
from home.models import Order, Aboutus, Chef, ContactMessage, Comment_cheff
from product.forms import OrderForm
from product.models import Category, Product, Images, Comment


def home(request):
    category = Category.objects.all()
    product_latest = Product.objects.all().order_by('-id')
    product_slayder = Product.objects.all().order_by('id')
    blog = Blog.objects.all()
    product_all = Product.objects.all().order_by('?')[:3]
    product_all1 = Product.objects.all().order_by('?')[:1]
    chef = Chef.objects.all()
    context = {
        'category': category,
        'product_latest': product_latest,
        'product_slayder': product_slayder,
        'blog': blog,
        'product_all': product_all,
        'product_all1': product_all1,
        'chef': chef,
    }
    return render(request, 'nmadur.html', context)


def product_detail(request, id, slug):
    product = Product.objects.get(pk=id)
    category = Category.objects.all().order_by('id')
    product_all = Product.objects.all().order_by('?')[:3]
    product_all1 = Product.objects.all().order_by('?')[:1]
    product_alle = Product.objects.all().order_by('?')[:4]
    product_one = Product.objects.all().order_by('?')[:6]
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, )
    form = OrderForm(request.POST)
    if form.is_valid():
        data = Order()
        data.name = form.cleaned_data['name']
        data.surname = form.cleaned_data['surname']
        data.phone = form.cleaned_data['phone']
        data.amount = form.cleaned_data['amount']
        data.category = form.cleaned_data['category']
        data.food = form.cleaned_data['food']
        data.address = form.cleaned_data['address']
        data.ip = request.META.get('REMOTE_ADDR')
        data.save()
        messages.success(request, "Siz Taom zakaz qildingiz aperato'r siz bilan bog'lanadi")
        return redirect('home')
    form = OrderForm
    context = {
        'form': form,
        'product': product,
        'product_all': product_all,
        'product_all1': product_all1,
        'product_alle': product_alle,
        'product_one': product_one,
        'images': images,
        'category': category,
        'comments': comments,
    }
    return render(request, 'product_details.html', context)


def category_product(request, id, slug):
    category = Category.objects.all()
    product_latest = Product.objects.all().order_by('-id')[:8]
    product_late = Product.objects.all().order_by('id')
    product_four = Product.objects.all().order_by('?')[:4]
    product_one = Product.objects.all().order_by('?')[:1]
    # catdata = Category.objects.get(pk=1)
    products = Product.objects.filter(category_id=id)
    paginator = Paginator(products, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        # 'catdata': catdata,
        'product_one': product_one,
        'products': products,
        'product_four': product_four,
        'product_latest': product_latest,
        'product_late': product_late,

    }
    return render(request, 'menu.html', context)


def aboutus(request):
    category = Category.objects.all()
    aboutus = Aboutus.objects.all()
    product = Product.objects.all()
    chef = Chef.objects.all()
    blog = Blog.objects.all()
    product_all1 = Product.objects.all().order_by('?')[:1]
    context = {
        'aboutus': aboutus,
        'chef': chef,
        'category': category,
        'product': product,
        'blog': blog,
        'product_all1': product_all1,
    }
    return render(request, 'about.html', context)


def cheff(request):
    chefs = Chef.objects.all()
    context = {
        'chefs': chefs,
    }
    return render(request, 'cheff.html', context)


def cheff_detail(request, id):
    chef = Chef.objects.get(pk=id)
    category = Category.objects.all()
    product_alle = Product.objects.all().order_by('?')[:4]
    chefs = Chef.objects.get(pk=id)
    comment_cheff = Comment_cheff.objects.filter(cheff_id=id)
    context = {
        'chefs': chefs,
        'category': category,
        'product_alle': product_alle,
        'chef': chef,
        'comment_cheff':comment_cheff,
    }
    return render(request, 'Cheff_detail.html', context)

def comment_cheff(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Comment_detail_Form(request.POST)
        if form.is_valid():
            data = Comment_cheff()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.cheff_id = id
            data.save()
            messages.success(request, "Sizning izohingiz qabul qilindi !")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning xabaringiz yuborildi! Rahmat")
            return redirect('home')
    form = ContactForm
    category = Category.objects.all()
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'contact.html', context)

