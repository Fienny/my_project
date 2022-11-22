from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostsList(ListView):
    model = Post
    ordering = 'heading'
    template_name = 'posts.html'
    context_object_name = 'posts'


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'

