from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails
# Create your views here.


# UserDetails = UserDetails.objects.all()
@login_required
def resumeDetail(request,pk):
  #  UserDetails = UserDetails.objects.filter(user_id=request.user.id)
    UserDetails =UserDetails.objects.get(id=pk)
    return render(request,'index.html',{'userDetails': UserDetails})



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