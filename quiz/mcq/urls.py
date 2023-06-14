
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
  
   path('',views.get_quiz,name='get_quiz'),
   path('home/',views.home,name='home'),
   path('quiz/',views.quiz,name='quiz'),
    path('questions/', views.question_list, name='question_list'),
    path('calculate-marks/', views.calculate_marks, name='calculate_marks'),
]
