from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm



class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(View):
    def get(self, request, self):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForms(instanse=tag)
        return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForms(request.POST, instanse=tag)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts' : posts})
