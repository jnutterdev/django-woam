from django.views.generic import ListView, DetailView, TemplateView, View
from django.http import HttpResponse
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    paginate_by = 6

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class AboutDetailView(TemplateView):
    template_name = "about.html"

class ColorView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('New color')
