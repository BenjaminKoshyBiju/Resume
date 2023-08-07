from django.shortcuts import render,redirect,get_object_or_404,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails,Education,Experience,Projects
from .forms import ResumeDetailsForm,EducationForm,ExperienceForm,ProjectForm
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
    
    form = ResumeDetailsForm() #was getting error that why added
    formExp= ExperienceForm()
    formEdu= EducationForm()
    formPro= ProjectForm()
    if request.method=='POST':
        form = ResumeDetailsForm(request.POST, request.FILES)
        formExp = ExperienceForm(request.POST, request.FILES)
        formEdu = EducationForm(request.POST, request.FILES)
        formPro = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
        if formExp.is_valid():
            formExp.save()
        
        if formEdu.is_valid():
            formEdu.save()

        if formPro.is_valid():
            formPro.save()
                
            return redirect('resume')  


    return render(request, 'resume_det.html', {'form': form})
        # personal_data = get_object_or_404(UserDetails, id=request.POST.get('user_id'))
        # experience=get_object_or_404(Experience, id=request.POST.get('user_id'))
        # education=get_object_or_404(Education, id=request.POST.get('user_id'))
        # projects=get_object_or_404(Projects, id=request.POST.get('user_id'))
    #     first_name = request.POST['first_name']
    #     last_name=request.POST['last_name']
    #     address=request.POST['address']
    #     email=request.POST['email']
    #     interests=request.POST['interests']
    #     phone = request.POST['phone']
    #     img=request.POST['img']


    #     heading=request.POST['first_name']
    #     pImg=request.POST['first_name']
    #     desc=request.POST['first_name']


    #     title=request.POST['first_name']
    #     companyName=request.POST['first_name']
    #     data=request.POST['first_name']
    #     date=request.POST['first_name']

    #     collegeName=request.POST['first_name']
    #     date=request.POST['first_name']
    #     degree=request.POST['first_name']

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