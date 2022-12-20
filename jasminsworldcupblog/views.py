from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Item
from .forms import CommentForm, PostForm
from django.contrib import messages



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        bookmarked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        if post.bookmark.filter(id=request.user.id).exists():
            bookmarked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                "commented": False,
                'liked': liked,
                "comment_form": CommentForm(),
                "bookmarked": bookmarked,
            }, 
                
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                "commented": True,
                'liked': liked,
                "comment_form": CommentForm(),
            }, 
                   )

class About(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'about.html',
        )

class Donate(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'donate.html',
        )

class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(self.request.user)
            liked = False
        else:
            post.likes.add(self.request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class bookmark(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.bookmark.filter(id=request.user.id).exists():
            post.bookmark.remove(self.request.user)
            # bookmarked = False
        else:
            post.bookmark.add(self.request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def add_item(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('PostList')
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add_item.html', context)


def edit_item(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect('PostList')
    form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'edit_item.html', context)


def toggle_item(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST)
    if request.method == 'POST':
        post.done = not post.done
        form.save()
        return redirect('PostList')

def delete_item_view(request, slug):
    text_type = 'post'
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post,'text_type': text_type} 
    return render(request, 'delete_item.html', context)


def delete_post(request, slug):
    """ Method to delete a post"""
    post = get_object_or_404(Post, slug=slug)
    if post.author.id == request.user.id:
        post.delete()
        messages.success(request, "Post deleted! Feel free to post a new one")
        return (redirect("home"))

def profile(request):
    bookmark_post = Post.objects.filter(bookmark=request.user)
    context = {
        'bookmark_post': bookmark_post
    }
    return render(request, 'profile.html', context)
