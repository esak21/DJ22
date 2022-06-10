from django.shortcuts import redirect, render
from .models import Profile, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.

def profiles (request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles 
    }
    return render(request, 'users/profiles.html', context = context)

def userProfiles (request,pk):
    profile = Profile.objects.get(id=pk)

    ## Skills have description 
    top_skills = profile.skill_set.exclude(description__exact = "")
    other_skills = profile.skill_set.filter(description="")
    print(profile)
    context = {
        'profile': profile ,
        "topskills": top_skills,
        "otherskills": other_skills
    }
    print(context)
    return render(request, 'users/user-profile.html', context = context)

from django.contrib.auth import login, authenticate, logout

def registerUser(request):
    page='register'
    # lets use the inbuilt user creation Form 
    # Model Form based on the user 
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Check if all the data is available or data has been manipulated or not 
            # we are saving the User in the Temporary instance in DATABASE and it wont be commited 
            # 
            user = form.save(commit=False)
            user.username = user.username.lower()
            # Save the user to Database 
            user.save()
            messages.success(request, "user was created sucessfully" )
            # make the user to Login automatically 
            #  we are adding some cookies to it 
            login(request, user)
            return redirect ( 'profiles')
        else: 
            messages.error(request , "Error Occured during registration ")

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context )

def logoutUser(request):
    # we are going to delete the session from the browser and user is nomore logged in
    logout(request)
    messages.info(request, "User was logout")
    # Return the user to the Login Pabge
    return redirect('login')

# view for Login 
def loginUser(request):
    page="login"
    # if the user is authenticated then we are going to traverse the user to the profile Page
    # if the user is loggedin already it wont go to the login Page
    if request.user.is_authenticated:
        return redirect('profiles')
    ## if the request Method is POST 
    ## from the POST request we get the username and password 
    if request.method == "POST":
        print(request.POST)  # <QueryDict: {'csrfmiddlewaretoken': ['pliMNjmBTL0QqX5YqXQFlL8YFnHl2yNwSBjwqEnugLtuUaKTl0rDmSAcgsovI8xn'], 'username': ['kumaresan'], 'password': ['MyManager@123']}>
        username = request.POST['username']
        password = request.POST['password']

        try: 
            user = User.objects.get(username=username) # checking if the user in database 
        except:
            messages.error(request, 'user name not available in Database')
        # authenticate is a inbuilt Method which checks the username and password cross verified against the Database 
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) # login will create a seesion for the user in the database, it will get the seesion and add to browser cookies 
            return redirect('profiles')
        else:
            # if the user name is wrong we are going to display it as message in the html 
            messages.error(request, "Username or password is incorrect")

    return render(request, 'users/login_register.html')