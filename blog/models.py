from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default='DMC')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
#        ordering = ["-created_on", "author"]
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title} | written by {self.reviewer}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.reviewer}"

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

