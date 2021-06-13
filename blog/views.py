from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# .models oznacza biezacy katalog, views i models sa w tym samym katalogu wiec mozemy uzyc . i nazwy pliku bez .py
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import redirect


# posts to nazwa QuerySetu, pozniej musimy przekazac to do szablonu
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id=pk).order_by('published_date')
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def comment_new(request, pk):
    if request.method == "POST":
        # tworzenie formularza
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.published_date = timezone.now()
            comment.save()
            return redirect('post_list')
    # formularz
    else:
        form = CommentForm()

    return render(request, 'blog/comment_new.html', {'form': form})

def callendar(request):
    return render(request, 'blog/terminarz.html', {'title': 'Terminarz'})

#def comment_list(request):
  #  comments = Comment.objects.all().order_by('published_date')
  #  return render(request, 'blog/post_details.html', {'comments': comments})