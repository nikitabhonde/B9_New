from django.contrib import messages                                # import messages
from django.contrib.auth import authenticate, login, logout        # add this for login fun
from django.contrib.auth.forms import AuthenticationForm           # add this for login fun
from django.shortcuts import HttpResponse, redirect, render

from .forms import NewUserForm
import logging


# # . means inside the same app
# Create your views here.

log = logging.getLogger("first")


def user_signup(request):
    if request.method == "POST":
        data = request.POST
        form  = NewUserForm(data)
        if form.is_valid():
            # yaha jo .save() method use ho rhi hai vo method humne forms.py mai override ki hai(ie. jo by-default .save() method hoti hai UserCreationForm kai pass vo hum use nhi kr rhe)
            user = form.save()          # user entry in auth_user in database table
            print(user)                 # user means username mila (ie RutujaB)
            messages.success(request, f"User '{user.username}' registered successfully...! You can login here.")
            return redirect("user_login")
        else:
            messages.warning(request, "Unsuccessful registration. Invalid information.") 
            return redirect("user_login")      # If anything is wrong in our site will get this error
    
    elif request.method == "GET":
        form = NewUserForm()
        return render(request=request, template_name="register.html", context={"signup_form":form})




def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)    # username, password
        if form.is_valid():
            username = form.cleaned_data.get("username")           # this fetch username from website   # RutujaB
            password = form.cleaned_data.get("password")           # this fetch password from website   # Python@123
            print(username, password)
            user = authenticate(username=username, password=password)       # this compare "fetch username & password from website" with actual username & password from database(verify) -- return user
            if user:
                login(request, user)                                        # login session maintain krta hai -- django session table in database
                messages.success(request, f"Hello {user.username}! You have been logged in sucessfully.")
                log.info("Logged in sucessfully.")
                return redirect("home_page")
        else:
            # # 2ways to show errors
            # for error in list(form.errors.values()):
            #     messages.error(request, error) 
            log.error("Invalid user_name or pass_word.")
            messages.error(request, "Invalid user_name or pass_word.")
        

    # elif request.method == "GET":
    return render(request=request, template_name="login.html", context={"login_form": AuthenticationForm()})



def user_logout(request):          # only request is imp not user
    logout(request=request)        # it delete all data related to user in that particular session
    messages.warning(request, "Logged out successfully!")
    return redirect("user_login")