from django.contrib import admin
from .models import *

class AdminAuthors(admin.ModelAdmin):
    list_display = ('name','description')


class AdminAffiliation(admin.ModelAdmin):
    list_display = ('name','about','url')

class AdminBlogs(admin.ModelAdmin):
    list_display = ('title','categorie','published','authenticated')

class AdminSuBlogs(admin.ModelAdmin):
    list_display = ('title','created_at','published')

class AdminBlogsFolio(admin.ModelAdmin):
    list_display = ('name','image')

class AdminCategories(admin.ModelAdmin):
    list_display = ('name','slug','created_at')

class AdminTags(admin.ModelAdmin):
    list_display = ('name','categorie')

admin.site.register(Authors,AdminAuthors)

admin.site.register(Affiliation,AdminAffiliation)

admin.site.register(Blogs,AdminBlogs)

admin.site.register(Sublogs,AdminSuBlogs)

admin.site.register(BlogsFolio,AdminBlogsFolio)

admin.site.register(Tags,AdminTags)

admin.site.register(Categories,AdminCategories)

admin.site.register(Newsletters)