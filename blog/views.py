from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post



# Create your views here.
#def my_blog(request):
#    return HttpResponse("<h1>Book Review Blog</h1> <uL><li>1.</li><li>2.</li><li>3.</li></ul>")

class PostList(generic.ListView):
    queryset = Post.objects.all().filter(status=1).order_by("-created_on")
#    template_name = "post_list.html"
# status = 1 : not in draft 
      