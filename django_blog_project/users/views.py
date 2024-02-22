from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("Valid User")
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is created for {username}')
            form.save()
            return redirect('blog-home')
        else:
            print("Invalid User")
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    context = {'form' : form}
    return render(request, 'users/register.html', context=context)
 