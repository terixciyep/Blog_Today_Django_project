from django import forms
from django import forms
from blogs.models import Blog, Category, Comment
from users.models import Users

class BlogCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'first_name_reg', 'id': 'title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'last_name_reg', 'id': 'description'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'username_reg', 'id': 'content'}))
    date_posted = forms.DateTimeField(widget=forms.HiddenInput())
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'password2_reg', 'id': 'category'}))
    author = forms.ModelChoiceField(queryset=Users.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Blog
        fields = ['title', 'description', 'content', 'date_posted', 'category', 'author']

class CommentForm(forms.ModelForm):
    text = forms.Textarea()
    comment_author = forms.ModelChoiceField(queryset=Users.objects.all(), widget=forms.HiddenInput())
    blod_id = forms.ModelChoiceField(queryset=Blog.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ['text','comment_author', 'blod_id']