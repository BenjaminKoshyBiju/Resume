from django.shortcuts import render,redirect,redirect
from .models import UserDetails,Education,Experience,Projects
from .forms import ResumeDetailsForm,EducationForm,ExperienceForm
# Create your views here.



def resume(request):
  #  UserDetails = UserDetails.objects.filter(user_id=request.user.id)
   

    return render(request, 'index.html', )




def resumeDetail(request):
    
    form = ResumeDetailsForm() #was getting error that why added
    
    # formEdu= EducationForm()
    # formPro= ProjectForm()
    # Check if an entry already exists for the user
  
    if request.method=='POST':
      
    
        
        # if form.is_valid():
        #     form.save()
        #     return redirect('resume') 
        user_to_update = UserDetails.objects.get(id=14)
        update_form = ResumeDetailsForm(request.POST,request.FILES, instance=user_to_update)
        if update_form.is_valid():
                update_form.save()
                return redirect('experience')




    details = UserDetails.objects.all() 
    form_list = [ResumeDetailsForm(instance=detail) for detail in details]
    return render(request, 'resume_det.html', {'form_list': form_list})
      

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




def eduForm(request):
      
    if request.method=='POST':
         # Handle delete action
        delete_id = request.POST.get('delete_id')
        if delete_id:
            education_to_delete = Education.objects.get(id=delete_id)
            education_to_delete.delete()
            return redirect('education') 
        #update the form
        update_id = request.POST.get('update_id')
        if update_id:
            education_to_update = Education.objects.get(id=update_id)
            update_form = EducationForm(request.POST, instance=education_to_update)
            if update_form.is_valid():
                update_form.save()
                return redirect('resume')
         #create new experience   
        form_list = EducationForm(request.POST)
        if form_list.is_valid():
            form_list.save()
            return redirect('resume')
        
        
       
   
        # if request.method == 'POST':
        #     delete_id = request.POST.get('delete_id')
        #     if delete_id:
        #         record_to_delete = Experience.objects.get(id=delete_id)
        #         record_to_delete.delete()
        #         return redirect('resume') 
    edus = Education.objects.all() 
    form_list = [EducationForm(instance=edu) for edu in edus]
    return render(request, 'education.html', {'form_list': form_list})



def projectForm(request):
    if request.method == 'POST':
        delete_id = request.POST.get('delete_id')
        if delete_id:
            project_to_delete = Projects.objects.get(id=delete_id)
            project_to_delete.delete()
            return redirect('project')

        update_id = request.POST.get('update_id')
        if update_id:
            project = Projects.objects.get(id=update_id)
            project.heading = request.POST.get(f'heading_{update_id}')
            project.desc = request.POST.get(f'desc_{update_id}')
            img_file = request.FILES.get(f'img_{update_id}')
            if img_file:
                project.img = img_file
            project.save()

        new_heading = request.POST.get('new_heading')
        new_img = request.FILES.get('new_img')
        new_desc = request.POST.get('new_desc')
        if new_heading and new_desc and new_img:
            new_project = Projects(heading=new_heading, img=new_img, desc=new_desc)
            new_project.save()

        return redirect('resume')

    projects = Projects.objects.all()
    return render(request, 'projects.html', {'projects': projects})




