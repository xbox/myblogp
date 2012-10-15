# Create your views here.
from django.shortcuts import render_to_response
from mybloga.models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render_to_response("blog_list.html",{"blogs":blogs})