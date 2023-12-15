from django.shortcuts import render,HttpResponse
from . models import UsersProfile,courses,Lessons,Reviews
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.
def index(request):
    return render(request,'index.html')
def cart(request):
    return render(request,'cart.html')
def student_dashboard(request):
    return render(request, 'dashboard/student-dashboard.html')
def dashboard(request):
    return render(request,'dashboard/student-dashboard.html')

def student_profile(request):
    
    profile=UsersProfile.objects.get(user=request.user)
    print(profile.user.first_name)
    return render(request,'dashboard/student-profile.html',{'profile':profile})

def course(request):
    
    course=courses.objects.all()
    return render(request,'course.html',{'course':course})


def student_enrolled_courses(request):
    return render(request,'dashboard/student-enrolled-courses.html')


def login_view(request):
    
    if request.method == "POST":
        if 'btn' in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            user = authenticate(request,username=username,password=password)
            
            if user is not None: 
                login(request, user)
                return render(request,'dashboard/student-dashboard.html')
            else:
                return HttpResponse("Invalid username or password")
        return render(request,'login.html')
    else:
        return render(request,'login.html')

def student_settings(request):
    return render(request,'dashboard/student-settings.html')

def sign_up(request):
    if  request.method =="POST":
        if 'register' in request.POST:
        #user field
            First_Name=request.POST.get("First_Name")
            Last_Name=request.POST.get("Last_Name")
            Email=request.POST.get("Email")
            Password=request.POST.get("Password")
            username = request.POST.get("Email")
        
            user=User.objects.create_user(first_name=First_Name,last_name=Last_Name,email=Email,password=Password,username=username)
        #usersprofile
        #linking user to userprofile
            user=user
        
            phone=request.POST.get("Phone")
            Upload_Profile_Picture=request.FILES.get("Upload Profile Picture")
    
            query=UsersProfile.objects.create(user=user,phone_number=phone,profile_picture=Upload_Profile_Picture)
        
       
    return render(request,'Login.html')

def course_details(request,slug):
    course_de=courses.objects.get(slug=slug)
    
    if request.method == 'POST' and 'submit' in request.POST:
        current_user = request.user
        rating = request.POST.get("rating")  
        review_text = request.POST.get("comment")  
        Reviews.objects.create(user=current_user,course=course_de,rating=rating,review_text=review_text)
       
    
    for less in course_de.lessons_set.all():
        print(less.lesson_title)
        for video in less.video_set.all():
            print(video.video_title)
    return render(request,'course-details.html',{'course_de':course_de})


def lessons(request,slug):
    course=courses.objects.get(slug=slug)
    for less in course.lessons_set.all():
        for video in less.video_set.all():  # Use the related_name 'videos'
            print(video.video_title)
    return render(request,'lesson.html',{'course':course})

def checkout(request):
    return render(request,"checkout.html")

def cart(request):
    return render(request,"cart.html")