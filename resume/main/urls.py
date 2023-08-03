from .import views
from django.urls import path
urlpatterns = [
     path('<str:pk>',views.resumeDetail,name='Detail'),
     path('login/', views.login_view, name='login'),
     path('register/', views.register_view, name='register'),
    
]