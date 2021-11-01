from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from .forms import PostForm
from .models import Post


class BlogView(View):
    """Главная блога"""
    template = 'blog/index.html'

    def get(self, request, *args, **kwargs):
        # Поиск
        query = self.request.GET.get('q')
        if query:
            posts = Post.objects.filter(Q(intro__icontains=query) | Q(text__icontains=query))
        # Вывод всех новостей
        else:
            posts = Post.objects.all()
        # Пагинация
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template, context={'page_obj': page_obj})


class PostView(View):
    """Страница поста"""
    template = 'blog/post.html'

    def get(self, request, post_id, *args, **kwargs):
        return render(request, self.template, context={'post': Post.objects.get(pk=post_id)})


class PostDetailsView(View):
    """Страница создания (редактирования) поста"""
    template = 'blog/post_details.html'

    def get(self, request, *args, **kwargs):
        form = PostForm(instance=Post.objects.get(pk=kwargs['post_id'])) if 'post_id' in kwargs else PostForm()
        return render(request, self.template, context={'form': form})

    def post(self, request, *args, **kwargs):
        if 'post_id' in kwargs:
            form = PostForm(request.POST, instance=Post.objects.get(pk=kwargs['post_id']))
        else:
            form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        return render(request, self.template, context={'form': form})


class PostDelete(View):
    """Удаление записи блога"""
    @staticmethod
    def get(request, post_id, *args, **kwargs):
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('blog')
