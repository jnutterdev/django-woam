from django.urls import path
from .views import BlogListView, BlogDetailView, AboutDetailView

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("about", AboutDetailView.as_view(), name="about"),
    path("", BlogListView.as_view(), name="home"),
]