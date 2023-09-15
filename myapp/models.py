from django.db import models
from django import froms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
         
class UserProfileEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        
def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


def profile_edit_view(request):
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            
    else:
        form = UserProfileEditForm(instance=request.user)
    return render(request, 'profile_edit.html', {'form': form})