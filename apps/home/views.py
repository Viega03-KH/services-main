from django.shortcuts import render
from blog.models import Post

def HomeViews(request):
    data = Post.objects.all()
    return render(request, 'pags/home-2.html', { 'data':data })