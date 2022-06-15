from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    paginate_by = 6

class BlogDetailView(DetailView):
    model = Post
    template_name = "partials/_post_detail.html"

class AboutDetailView(TemplateView):
    template_name = "about.html"

