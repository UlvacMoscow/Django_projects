from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import Post, Tag
from .utils import ObjectdetailMixin



class PostDetail(ObjectdetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectdetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts' : posts})
