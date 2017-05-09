from django.shortcuts import render
# Create your views here.
from django.views import generic
from fullstack.settings import POSTS_DIR, BASE_DIR
import os

class BlogView(generic.TemplateView):
    #Read post directory
    #post_dir = "../posts"



    template_name = "yblog/blog.html"

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        posts=[]
        for filename in os.listdir(POSTS_DIR):
            if filename.endswith(".md") or filename.endswith(".markdown"):
                # print(os.path.join(directory, filename))
                with open(os.path.join(POSTS_DIR, filename), 'r') as mdfile:
                    posts.append(mdfile.read())
        if len(posts) > 0:
            context['posts'] = posts
        else:
            context['posts'] = "No post"
        return context