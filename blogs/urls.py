from django.urls import path
from .views import blogs,portfolio,detail,postcomment,testimonials
urlpatterns = [
	path('testimonials/',testimonials,name="testimonial"),
	path('',blogs,name="blogs"),
	path('portfolio/',portfolio,name="portfolio"),
	path('<str:slug>/',detail,name="detail"),
	path('post/comment/',postcomment,name="postcomment"),

]