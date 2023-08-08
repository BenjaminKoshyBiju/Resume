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
    
    formEdu= EducationForm()
    formPro= ProjectForm()
    if request.method=='POST':
        form = ResumeDetailsForm(request.POST, request.FILES)
        
        formEdu = EducationForm(request.POST, request.FILES)
        formPro = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.user = request.user  # Assign the logged-in user
            new_entry.save()
            return redirect('experience') 
        
        if formEdu.is_valid():
            formEdu.save()
            return redirect('resume') 

        if formPro.is_valid():
            formPro.save()
            return redirect('resume')  




    return render(request, 'resume_det.html', {'form': form})
      

def expForm(request):
    formExp= ExperienceForm()
    if request.method=='POST':
        formExp = ExperienceForm(request.POST, request.FILES)
        if formExp.is_valid():
            new_entry = formExp.save(commit=False)
            new_entry.user = request.user
            new_entry.save()
            return redirect('resume')  
    return render(request, 'experience.html', {'formExp': formExp})

    



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