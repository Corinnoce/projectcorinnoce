from django.shortcuts import render,redirect
from blogs.models import Blogs,get_articles,Newsletters,paginate_objects
from accounts.models import Crypto
from django.core.mail import send_mail

def sendmailnow():
    pass

 
def index(request):
    articles = paginate_objects(request,get_articles(request),8) 
    #Crypto.objects.create_user(username="Corinnoce",password="annabella#n4",is_superuser=True,is_staff=True)
    return render(request,'index.html',{'articles':articles})

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        _,_=Newsletters.objects.get_or_create(email=email)
        return redirect('index')

def NotFound(request,exception):
    return render(request,'404.html')
