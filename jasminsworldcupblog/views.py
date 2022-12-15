from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Item
from .forms import CommentForm, ItemForm



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
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PostList')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('PostList')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('PostList')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('PostList')

def profile(request):
    bookmark_post = Post.objects.filter(bookmark=request.user)
    context = {
        'bookmark_post': bookmark_post
    }
    return render(request, 'profile.html', context)

