from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
import random
from django.http import HttpResponseRedirect
from django.urls import reverse




def home(request):
     
     categories = Category.objects.all()

     if request.GET.get('categori'):
          return redirect(f"/quiz/?categori={request.GET.get('categori')}")

     return render(request,'home.html' , { 'categories' : categories})


def quiz(request):
     context = { 
          'category' : request.GET.get('categori')
     }
     return render(request,'quiz.html',context)


def get_quiz(request):
    try:
 
           question_objs = Question.objects.all()

           if request.GET.get('categori'):
                question_objs = question_objs.filter(category__category__name__icontains=request.GET.get('categori'))

           data = []
           random.shuffle(list(question_objs))
        

           for question_obj in question_objs:
                
                
                data.append ({
                     "uid" : question_obj.uid,
                     "category" : question_obj.category.category_name,
                     "question" : question_obj.question,
                     "marks" : question_obj.marks,
                     "answers" : question_obj.get_answer(),
                     
                })

           payload = { 'status' : True , 'data' : data }

           return JsonResponse(payload)
           

    except Exception as e:
        print(e)
    return HttpResponse("somwthing went wrong")



def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})



def calculate_marks(request):
    if request.method == 'POST':
        question_uids = [key.split('_')[1] for key in request.POST.keys() if key.startswith('question_')]
        total_marks = 0

        for question_uid in question_uids:
            selected_answer_uid = request.POST.get(f'question_{question_uid}')
            selected_answer = Answer.objects.get(uid=selected_answer_uid)

            if selected_answer.is_correct:
                total_marks += selected_answer.questions.marks

        return render(request, 'result.html', { 'marks': total_marks})
 
    return redirect(reverse('question_list'))