from django.urls import path

from . import views

app_name = 'kmsurvey'
urlpatterns = [
    path('', views.index, name='index'),
    path('approach_survey/', views.ApproachSurveyView, name='approachSurvey'),
]
