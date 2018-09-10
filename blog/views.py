# blog/views.py
from django.shortcuts import get_object_or_404, render
from .models import Post

# def post_list(request):
#     return render(request, 'blog/post_list.html')

def post_list(request):
    qs = Post.objects.all()  # 아직 db에 접근한 것 아님.
    
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {'post_list': qs, 'q':q})

def post_detail(request, id):
   # try:
   #    post = Post.objects.get(id=id)
   # except Post.DoesNotExist:
   #    raise Http404
   
   post = get_object_or_404(Post, id=id)
   return render(request, 'blog/post_detail.html', {'post' : post})
    