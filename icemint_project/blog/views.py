from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import User, Post


class UsersListView(ListView):
    model = User


class PostsListView(ListView):
    model = Post

    def dispatch(self, *args, **kwargs):
        self.author = get_object_or_404(User, pk=kwargs['user_id'])
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context

    def get_queryset(self):
        current_user = self.request.user

        posts = Post.objects.filter(author=self.author.id).\
            order_by('-created').select_related('author')

        if self.author.id != current_user.id and not current_user.is_staff:
            posts = posts.filter(published=True)

        return posts


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        current_user = self.request.user

        post = super().get_object(queryset)

        if not post.published and not current_user.is_staff \
                and post.author.id != current_user.id:
            raise Http404

        return post

    def get_queryset(self):
        return super().get_queryset().select_related('author')


class PostCreateView(CreateView):
    model = Post
    fields = [
        'title',
        'text',
        'published',
    ]

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = [
        'title',
        'text',
        'published',
    ]

    def get_object(self, queryset=None):
        current_user = self.request.user

        post = super().get_object(queryset)

        if not current_user.is_staff and post.author.id != current_user.id:
            raise Http404

        return post
