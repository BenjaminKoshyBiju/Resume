from .import views
from django.urls import path
urlpatterns = [
     path('',views.resume,name='resume'),
     # path('details/',views.resumeDetail,name='Detail'),
     # path('details/experience/',views.expForm,name='experience'),
     # path('details/education',views.eduForm,name='education'),
     # path('details/project',views.projectForm,name='project'),
   
    
]
