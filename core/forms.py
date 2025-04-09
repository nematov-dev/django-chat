from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

from room.models import Room

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
