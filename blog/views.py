from django.views.generic import ListView, DetailView, TemplateView
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

# Create your views here.

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    paginate_by = 6

class BlogDetailView(DetailView):
    model = Post
    template_name = "partials/_post_detail.html"

class AboutDetailView(TemplateView):
    template_name = "about.html"

def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 2) # 2 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:     
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,'blog/post/list.html',{'page': page,'posts': posts, 'tag': tag})