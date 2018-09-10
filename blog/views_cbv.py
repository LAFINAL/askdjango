from django import forms
from django.views.generic import CreateView
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = '/asdf/asdf 원래 이렇게 제공해줘야함.'

post_new = PostCreateView.as_view()