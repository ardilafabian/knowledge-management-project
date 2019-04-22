from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the knowledge management index.")

def ApproachSurveyView(request):
    a = Approach.objects.filter(name='Grupal')
    #print(a)
    questions = Question.objects.filter(approach__id=2)
    print(questions)
    scale_choices = Scale_Choice.SCALE_CHOICES
    dicotomic_choices = Dicotomic_Choice.DICOTOMIC_CHOICES
    context = {
        'approach_questions': questions,
        'scale_choices': scale_choices,
        'dicotomic_choices' : dicotomic_choices,
    }
    return render(request, "kmsurvey/approachSurvey.html", context)
