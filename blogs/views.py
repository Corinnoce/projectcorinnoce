from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.core.paginator import Paginator
from django.urls import reverse
from django.db.models import Q


def blogs(request):
	articles = get_articles(request)
	if request.GET.get('article'):
		articles = Blogs.objects.filter(Q(title__icontains=request.GET.get('article'))|Q(description__icontains=request.GET.get('article')))
	if request.GET.get('tag'):
		articles = articles = Blogs.objects.filter(Q(title__icontains=request.GET.get('tag')) | Q(description__icontains=request.GET.get('tag')))
	articles = paginate_objects(request,articles,8)
	return render(request,'blogs/index.html',{'articles':articles,'categories':get_categories()})

def portfolio(request):
	articles = Blogs.objects.filter(thumbnail__isnull=False)
	categories = get_categories()[:5]
	return render(request,'blogs/portfolio.html',{'articles':articles,'categories':categories})

def detail(request,slug):
	article = get_object_or_404(Blogs,slug=slug,published=True)
	if not request.user.is_authenticated:
		article = get_object_or_404(Blogs,slug=slug,published=True,authenticated=False)
	comments = Comment.objects.filter(blog=article)
	article_link = Blogs.objects.filter(categorie=article.categorie,published=True).order_by('-created_at')[:5]
	context={}
	context['affilates'] = Affiliation.objects.filter(article=article)
	context['tags'] = Tags.objects.filter(categorie=article.categorie)
	context['article'] = article
	context['comments'] = comments
	context['categories'] = get_categories()
	context['article_link'] = article_link
	context['article_detail'] = Sublogs.objects.filter(blogs=article,published=True)
	context['article_folio'] = BlogsFolio.objects.filter(blogs=article)
	return render(request,'blogs/detail.html',context)

def postcomment(request):
	if request.method == "POST":
		
		if request.user.is_preminium:
			name = request.user.first_name
			email = request.user.email
		else:
			name = request.POST.get('name')
			email = request.POST.get('email')

		content = request.POST.get('comment')
		slug = request.POST.get('slug')
		blog = get_object_or_404(Blogs,slug=slug)
		Comment.objects.create(blog=blog,name=name,email=email,content=content)
		_,_=Newsletters.objects.get_or_create(email=email)
	return redirect(reverse('detail',kwargs={'slug':slug}))



	comment = get_object_or_404(Comment,id=id)
	return render(request,'blogs/response.html',{'comment':comment})

def testimonials(request):
	return render(request,'blogs/testimonial.html')

	
