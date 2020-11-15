from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .models import User
from django.contrib.auth import get_user_model


class UserCreateForm(UserCreationForm):

    class Meta(UserCreationForm):
        fields = ('username','email','password1','password2','description','profile_picture','birth_date')
        model = get_user_model()

        def __init__(self,*args,**kwargs):
            super().init(*args,**kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'E-Mail'
            
