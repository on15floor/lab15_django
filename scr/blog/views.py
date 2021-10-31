from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import View

from .forms import PostForm
from .models import Post


class BlogView(View):
    """Главная блога"""
    def get(self, request, *args, **kwargs):
        posts = get_list_or_404(Post)
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/index.html', context={'page_obj': page_obj})


class PostView(View):
    """Страница поста"""
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'blog/post.html', context={'post': post})


class PostCreateView(View):
    """Страница создания поста"""
    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, 'blog/post_details.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        return render(request, 'blog/post_details.html', context={'form': form})


class PostUpdateView(View):
    """Страница редактирования поста"""
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(instance=post)
        return render(request, 'blog/post_details.html', context={'form': form})

    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog')
        return render(request, 'blog/post_details.html', context={'form': form})


class PostDelete(View):
    """Удаление записи блога"""
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return redirect('blog')
