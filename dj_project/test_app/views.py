from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import View
from .models import Post
from .forms import PostForm


class PostsView(View):
    def get(self, request):
        form = PostForm()
        posts = Post.objects.all()
        context = {
            'form': form,
            'posts': posts,
        }

        return render(request, 'test_app/posts.html', context)

    def post(self, request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('test_app:posts', )

        # There should be another method if invalid form (:
