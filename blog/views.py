from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from blog.forms import Comment_detail_Form
from blog.models import Blog, Comment_blog
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from product.models import Category


def blog(request):
    category = Category.objects.all()
    blog = Blog.objects.all()
    paginator = Paginator(blog, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    context = {
        'blog' :blog,
        'category' :category,
        'blog_detail': blog_detail,
    }
    return render(request, 'blog.html', context)


def blog_detail(request ,id):
    blog = Blog.objects.all().order_by('?')[:4]
    category = Category.objects.all()
    blog_detail = Blog.objects.get(pk=id)
    comment_blog = Comment_blog.objects.filter(blog_id=id)
    context = {
        'category' :category,
        'blog_detail' :blog_detail,
        'comment_blog' :comment_blog,
        'blog' :blog,
    }
    return render(request, 'blog-detail.html', context)


def comment_blog(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Comment_detail_Form(request.POST)
        if form.is_valid():
            data = Comment_blog()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_id = id
            data.save()
            messages.success(request, "Sizning izohingiz qabul qilindi !")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)