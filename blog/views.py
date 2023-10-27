from django.forms import ImageField
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone 
from .models import Image, Post
from .forms import ImageForm, PostForm
from django.http import HttpResponse
import random


# Create your views here.

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})        
   


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', { 'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST": 
        form = PostForm(request.POST, instance=post)
        if form.is_vaild():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/post_edit.html', {'form': form})

def upload(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'blog/upload.html', {'image': Image})

    

def gatcha(request):
    return render(request, 'blog/gatcha.html')

def show_gatcha(request):
    all_images = Image.objects.all()
    random_image = random.choice(all_images)
    random_image_title = random_image.title
    return render(request,'blog/show_gatcha.html', {'random_image': random_image, 'random_image_title': random_image.title})
