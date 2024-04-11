from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ResisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1','password2','nickname','location','university']