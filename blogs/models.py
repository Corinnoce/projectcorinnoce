from django.db import models
from django.core.paginator import Paginator
from slugify import slugify

class Categories(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000,blank=True, null=True)
    image = models.ImageField(upload_to='images/categories/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Categories, self).save(*args, **kwargs) # Call the real save() method


class Authors(models.Model):
    name = models.CharField(max_length=500)
    profil = models.ImageField(upload_to='authors/profils/',blank=True, null=True)
    description = models.TextField(blank=True)
    facebook = models.CharField(max_length=50000, blank=True, null=True)
    discord = models.CharField(max_length=50000, blank=True, null=True)
    telegram = models.CharField(max_length=50000, blank=True, null=True)

    def __str__(self):
        return self.name



class Tags(models.Model):
    name = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categories,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=1000)
    categorie = models.ForeignKey(Categories,on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='images/blogs/',null=True,blank=True)
    description = models.TextField(blank=True)
    File = models.FileField(blank=True,null=True,upload_to='data/free/download/')
    author = models.ForeignKey(Authors,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=1000,unique=True,blank=True)
    published = models.BooleanField(default=False)
    authenticated = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(Blogs, self).save(*args, **kwargs) # Call the real save() method
       if self.published:
        print("Nouveau article creer")

class Sublogs(models.Model):
    blogs = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='images/Sublogs/',blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment (models.Model):
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=1000)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    
class BlogsFolio(models.Model):
    blogs = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='images/Sublogs/Folio/',blank=True, null=True)

    def __str__(self):
        return self.name

class Newsletters(models.Model):
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email

class Affiliation(models.Model):
    article = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    name = models.CharField(max_length=250,blank=True,null=True)
    url = models.CharField(max_length=2000)
    about = models.CharField(max_length=20000,blank=True,null=True)
    image = models.ImageField(upload_to='images/affilate/',blank=True, null=True)

    def __str__(self):
        return self.name

def paginate_objects(request,objects,nbre):
    paninator = Paginator(objects,nbre)
    page = request.GET.get('page')
    return paninator.get_page(page)

def get_articles(request):
	articles = Blogs.objects.filter(published=True,authenticated=False).order_by('-created_at')
	if categorie:=request.GET.get('categorie'):
		articles = Blogs.objects.filter(categorie=Categories.objects.get(slug=categorie),published=True).order_by('-created_at')
	return articles

def get_articles_authenticated(request):
	articles = Blogs.objects.filter(published=True,authenticated=True).order_by('-created_at')
	if categorie:=request.GET.get('categorie'):
		articles = Blogs.objects.filter(categorie=Categories.objects.get(slug=categorie),published=True).order_by('-created_at')
	return articles

def get_categories():
    return Categories.objects.all()
