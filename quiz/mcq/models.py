from django.db import models
import uuid
import random
# Create your models here.

class basemodel(models.Model):
    uid = models.UUIDField(primary_key= True, default=uuid.uuid4,editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
    
    

class Category(basemodel):
    category_name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.category_name
   

class Question(basemodel):
    category = models.ForeignKey(Category , related_name= 'category1' ,on_delete= models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=2)

    def __str__(self) -> str:
        return self.question
    
    def get_answer(self):
        answer_objs = list(Answer.objects.filter(questions = self))
        random.shuffle(answer_objs)
     
        data = []
    
        for answer_obj in answer_objs:
           data.append({
               
                   'answer' : answer_obj.answer,
                   'is_correct' : answer_obj.is_correct,

               })
           

    
        return data  
  

class Answer(basemodel):
    questions = models.ForeignKey(Question,related_name= 'question_answer',on_delete=models.CASCADE)

    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer

