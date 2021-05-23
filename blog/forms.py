# importujemy formularze django
from django import forms
# importujemy nasz model Post
from .models import Post


# PostForm to nazwa naszego formularza
# informujemy, ze ten formularz jest formularzem modelu (ModelForm)
class PostForm(forms.ModelForm):

    class Meta:
        # informujemy jaki model powinien byc wykorzystany do stworzenia tego formularza
        model = Post
        # i ktore pola powinny pojawic sie w formularzu
        fields = ('title', 'text',)

# pozniej uzyc ten formularz wewnatrz views.py, i wyswietlic w templates
# trzeba stworzyc: link do strony(post/new, 'post_new'), adres url, widok, szablon
# next>blog/base zmieniamy page-header