from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

# Create your views here.
#def my_blog(request):
#    return HttpResponse("<h1>Book Review Blog</h1> <uL><li>1.</li><li>2.</li><li>3.</li></ul>")

class PostList(generic.ListView):
    queryset = Post.objects.all().filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 4

# note: status = 1 : not in draft 

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
#    context = {"post": post, "Author": DMC}
    comments = post.comment.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )

    comment_form = CommentForm()
    return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_count": comment_count,
                "comment_form": comment_form,
            },
        )

  