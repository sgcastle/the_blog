from django.shortcuts import render
#from .models import About
# from .models import Post
#
# def home(request):
#     posts = Post.objects.order_by('pub_date')
#     return render(request, "posts/home.html", {'posts':posts})
#
# def post_details(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     return render(request, "posts/posts_detail.html", {"post":post})
def about(request):
    return render(request, "sitepages/about.html")
