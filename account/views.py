from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.
def register(request):
    if request.method=='POST':

        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'sorry username already exist')
            return redirect('register')

        elif User.objects.filter(email=email).exists():
            messages.info(request, "sorry email already exist")
            return redirect('register')

        else:

        
                user=User.objects.create_user(username=username, email=email,password=password)
                user.save()
                messages.success(request, f'Account created for {username}')
                print("user created")
                return redirect('/account/login')


    else:
        return render(request, 'register.html')



    


def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username=username ,password=password)

        if user is not None:
              auth.login(request,user)
             
              return redirect('/')
        else: 
             messages.info(request, 'invalid ')
             return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def  profile(request):
    return render(request, 'profile.html')
    
