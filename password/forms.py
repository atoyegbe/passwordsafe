from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm



class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'confirm your password'})
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']



