from .import views
from django.urls import path
urlpatterns = [
     path('',views.resume,name='resume'),
     path('login/', views.login_view, name='login'),
     path('register/', views.register_view, name='register'),
     path('details/',views.resumeDetail,name='Detail'),
     path('details/experience',views.expForm,name='experience'),
     path('details/education',views.resumeDetail,name='education'),
     path('details/project',views.resumeDetail,name='project'),

    
]