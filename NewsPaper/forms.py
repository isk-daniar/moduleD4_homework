from django.forms import ModelForm
from NewsPaper.news.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'category', 'title', 'text']