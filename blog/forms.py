from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'date_posted')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),

            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'date_posted': forms.DateInput(format='%d/%m/%Y'),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'date_posted')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'date_posted': forms.DateInput(format='%d/%m/%Y')

        }
