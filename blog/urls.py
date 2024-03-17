from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # Note: function-based view, as_view() method is not required :-
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
