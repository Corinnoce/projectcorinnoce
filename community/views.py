from django.shortcuts import render,redirect
from blogs.models import *
from community.models import Collection
from django.db.models import Q

def authenticated(request):
    articles = get_articles_authenticated(request)
    if request.GET.get('article'):
        articles = Blogs.objects.filter(Q(title__icontains=request.GET.get('article')) | Q(description__icontains=request.GET.get('article')))
    if request.GET.get('tag'):
        articles = Blogs.objects.filter(Q(title__icontains=request.GET.get('tag')) | Q(description__icontains=request.GET.get('tag')))
    articles = paginate_objects(request,articles,8)
    context = {}
    context['articles'] = articles
    context['title'] = "Nos meilleurs pour vous"
    context['categories'] = get_categories()
    return render(request,'blogs/index.html',context)

def add_to_collection(request,slug):
    if request.user.username:
        Collection.objects.get_or_create(slug=slug,user=request.user)
        return redirect('views-collection')
    return redirect('login')

def my_collections(request):
    if request.user.username:
        collections = Collection.objects.filter(user=request.user)
        if slug:=request.GET.get('slug'):
            return add_to_collection(request,slug)
        return render(request,'community/collections.html',{"collections":collections})
    return redirect('login')

def remove_collection(request,slug):
    collection = Collection.objects.get(slug=slug,user=request.user)
    collection.delete()
    #collection.save()
    print("Remove sucessfull :) !!!")
    return redirect('views-collection')

