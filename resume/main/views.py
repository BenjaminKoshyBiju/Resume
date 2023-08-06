from django.shortcuts import render,redirect,get_object_or_404,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails,Education,Experience,Projects
from .forms import ResumeDetailsForm
# Create your views here.


@login_required
def resume(request):
  #  UserDetails = UserDetails.objects.filter(user_id=request.user.id)
    user = request.user
    try:
        user_details = UserDetails.objects.get(user=user)
    except UserDetails.DoesNotExist:
        # Handle the case when user details are not found in the database
     user_details = None

    return render(request, 'index.html', {'user_details': user_details})




def resumeDetail(request):
    
    form = ResumeDetailsForm()

    if request.method=='POST':
        form = ResumeDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume')  # Replace 'success_url' with the URL to redirect after successful form submission


    return render(request, 'resume_det.html', {'form': form})
    #     personal_data = get_object_or_404(UserDetails, id=request.POST.get('user_id'))
    #     experience=get_object_or_404(Experience, id=request.POST.get('user_id'))
    #     education=get_object_or_404(Education, id=request.POST.get('user_id'))
    #     projects=get_object_or_404(Projects, id=request.POST.get('user_id'))
    #     first_name = personal_data.first_name
    #     last_name=personal_data.last_name
    #     address=personal_data.address
    #     email=personal_data.email
    #     interests=personal_data.interests
    #     phone = personal_data.phone
    #     img=personal_data.img


    #     heading=projects.heading
    #     pImg=projects.img
    #     desc=projects.desc


    #     title=experience.title
    #     companyName=experience.companyName
    #     data=experience.data
    #     date=experience.date

    #     collegeName=education.collegeName
    #     date=education.date
    #     degree=education.Degree

    #     personalData = UserDetails(first_name=first_name,last_name=last_name,img=img,address=address,
    #                                email=email,interests=interests,phone=phone)
    #     projectData=Projects(heading=heading,img=pImg,desc=desc)
    #     experienceData=Experience(title=title,companyName=companyName,data=data,date=date)
    #     educationData=Education(collegeName=collegeName,date=date,degree=degree)

    #     personalData.save()
    #     print("saved successfully")

    #     experienceData.save()
    #     print("saved successfully")

    #     projectData.save()
    #     print("saved successfully")

    #     educationData.save()
    #     print("saved successfully")
    #     return redirect('index.html')
    # else:     
    #     return render(request,'resume_details.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Detail')  
        else:
           
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})