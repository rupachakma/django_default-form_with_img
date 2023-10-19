from django.shortcuts import redirect, render
from myapp.forms import AddForm, LoginForm, SignupForm
from django.contrib import messages
from myapp.models import Posts
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def home(request):
    post=Posts.objects.all()
    return render(request,"home.html",{'post':post})


def dashboardpage(request):
    post = Posts.objects.all()

    return render(request,"dashboard.html",{'post':post})

def aboutpage(request):
    return render(request,"about.html")

def signuppage(request):
    error_messages = {
        'password_error':'Password and Confirm Password not match'
    }
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request,"Congratulations Successfully logged in..")
           return redirect("loginpage")
        else:
            messages.error(request,error_messages['password_error'])
            return redirect("signuppage")

    else:
        form = SignupForm()
    return render(request,"signup.html",{'form':form})


def loginpage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST )
            if form.is_valid():
                username = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=username,password=userpass)
                print(username, userpass)
                print(user)
                if user is not None:
                    login(request,user)
                    return redirect('homepage')
                else:
                    messages.error(request,"InValid your request")
        else:
            form = LoginForm()
        return render(request,"login.html",{'form':form})
    else:
        return redirect('homepage')

        

def addpage(request):
    if request.method == "POST":
        form = AddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboardpage")
    else:
        form = AddForm
    return render(request,"add.html",{'form':form})

def updatepage(request,id):
    post = Posts.objects.get(id=id)
    if request.method == "POST":
        form = AddForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect("dashboardpage")
    else:
        form = AddForm(instance=post)

    return render(request,"update.html",{'form':form})

def logoutpage(request):
    logout(request)
    return redirect("loginpage")

def deletepage(request,id):
    post=Posts.objects.get(id=id)
    post.delete()
    return redirect("dashboardpage")


