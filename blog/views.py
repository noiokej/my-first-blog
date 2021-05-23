from django.shortcuts import render
from django.utils import timezone
# .models oznacza biezacy katalog, views i models sa w tym samym katalogu wiec mozemy uzyc . i nazwy pliku bez .py
from .models import Post

# posts to nazwa QuerySetu, pozniej musimy przekazac to do szablonu
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})