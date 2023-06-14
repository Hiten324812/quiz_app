from django.contrib import admin

# Register your models here.

from .models import *


class questionsadmin(admin.StackedInline):
    model = Question




class answeradmin(admin.StackedInline):
    model  = Answer



class questionadmin(admin.ModelAdmin):
    inlines = [answeradmin]  

class cateadmin(admin.ModelAdmin):
  inlines = [questionsadmin]



admin.site.register(Category , cateadmin)
admin.site.register(Question , questionadmin)
admin.site.register(Answer)