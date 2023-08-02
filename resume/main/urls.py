from .import views
from django.urls import path
urlpatterns = [
     path('',views.resumeDetail,name='Detail'),
    #  path('', views.login_view, name='login'),
    #  path('register/', views.register_view, name='register'),
    
]