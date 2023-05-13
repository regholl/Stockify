from django.shortcuts import render,redirect
from .forms import CreateUserForm,ProfileForm,LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created! You can Login now!')
            return redirect('login')
    else:
        form =CreateUserForm()
    context = {'form':form}
    return render(request,'User.register.html',context)


