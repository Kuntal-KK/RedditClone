from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['pwd1'] == request.POST['pwd2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error_key1':'User Already Exists. Choose Another Name'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['pwd1'])
                # login(request,user)
                # return render(request, 'accounts/login.html')
                return redirect('accounts:loginview')
        else:
            return render(request, 'accounts/signup.html', {'error_key2':'Passwords Did Not Match'})
    else:
        return render(request,'accounts/signup.html')

def loginview(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['pwd1'])

        if user is not None:
            login(request,user)

            if 'next' in request.POST:
                return redirect(request.POST['next'])

            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error_key':'Username and Password Didn\'t Match'})

    else:
        return render(request, 'accounts/login.html')

@login_required
def logoutview(request):
    logout(request)
    return redirect('home')
