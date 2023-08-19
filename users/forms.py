from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from users.models import Users


class UserRegistrationFrom(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'first_name_reg', 'id': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'last_name_reg', 'id': 'last_name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username_reg', 'id': 'username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'email_reg', 'id': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password1_reg', 'id': 'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password2_reg', 'id': 'password2'}))

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class AuthUserForm(AuthenticationForm):
    class Meta:
        model = Users
        fields = ['username', 'password']


class ChangeUserForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'id': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'id': 'last_name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'id': 'email'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True, 'id': 'username'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control py-4', 'id': 'image'}),
                             required=False)

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'username', 'image']
