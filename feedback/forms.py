from django import forms
from django import forms
from blogs.models import Blog, Category, Comment
from users.models import Users
from feedback.models import feedback

class feedbackForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'first_name_reg', 'id': 'title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'last_name_reg', 'id': 'text'}))
    author = forms.ModelChoiceField(queryset=Users.objects.all(), widget=forms.HiddenInput())
    date_posted = forms.DateTimeField(widget=forms.HiddenInput())

    class Meta:
        model = feedback
        fields = ['title', 'text','author','date_posted']
