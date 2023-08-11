from django.shortcuts import render,redirect,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails,Education,Experience,Projects
from .forms import ResumeDetailsForm,EducationForm,ExperienceForm,ProjectForm
# Create your views here.


@login_required
def resume(request):
  #  UserDetails = UserDetails.objects.filter(user_id=request.user.id)
   

    return render(request, 'index.html', )




def resumeDetail(request):
    
    form = ResumeDetailsForm() #was getting error that why added
    
    # formEdu= EducationForm()
    # formPro= ProjectForm()
    # Check if an entry already exists for the user
  
    if request.method=='POST':
      
        # formEdu = EducationForm(request.POST, request.FILES)
        # formPro = ProjectForm(request.POST, request.FILES)
        form = ResumeDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume') 
        # if formEdu.is_valid():
        #     formEdu.save()
        #     return redirect('resume') 

        # if formPro.is_valid():
        #     formPro.save()
        #     return redirect('resume')  




    return render(request, 'resume_det.html', {'form': form})
      

def expForm(request):
   

    
    if request.method=='POST':
         # Handle delete action
        delete_id = request.POST.get('delete_id')
        if delete_id:
            experience_to_delete = Experience.objects.get(id=delete_id)
            experience_to_delete.delete()
            return redirect('experience') 
        #update the form
        update_id = request.POST.get('update_id')
        if update_id:
            experience_to_update = Experience.objects.get(id=update_id)
            update_form = ExperienceForm(request.POST, instance=experience_to_update)
            if update_form.is_valid():
                update_form.save()
                return redirect('resume')
         #create new experience   
        form_list = ExperienceForm(request.POST)
        if form_list.is_valid():
            form_list.save()
            return redirect('resume')
        
        
       
   
        # if request.method == 'POST':
        #     delete_id = request.POST.get('delete_id')
        #     if delete_id:
        #         record_to_delete = Experience.objects.get(id=delete_id)
        #         record_to_delete.delete()
        #         return redirect('resume') 
    experiences = Experience.objects.all() 
    form_list = [ExperienceForm(instance=experience) for experience in experiences]
    return render(request, 'experience.html', {'form_list': form_list})




