
from django.shortcuts import redirect,render
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.models import User

from store.forms import UserCreationForm,UserLoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout


class UserCreationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'store/auth/register.html'
    success_url = reverse_lazy('login')

def userloginview(request):
    context = {'form':UserLoginForm}
    template_name = 'store/auth/login.html'
    if request.user.is_authenticated:
        messages.warning(request,"Yor Are Already Logged in ")
        success_message = "Account Created Succesfuly"
        return redirect('collections')
        
    else:
        if request.method=="POST":           
            form = UserLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request,"Logged in Successfully")
                    success_message = "Acconty Created Succesfuly"
                    return redirect('collections')
                else:
                    messages.error(request,"Invalid Password or Username")
                    success_message = "Acconty Created Succesfuly"
                    return redirect('login')
        return render(request,template_name,context)

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Succesfully")
    return redirect('collections')

              


                