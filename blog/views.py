from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
  allBlogPosts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html', {'allPosts': allBlogPosts} )

def postDetail(request, pk):
  postToShow = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post.html', {'postToShow': postToShow})



