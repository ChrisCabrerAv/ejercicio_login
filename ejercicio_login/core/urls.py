from django.urls import path
from .views import HomeView, ExerciseView

core_patterns = ([
    path("", HomeView.as_view(), name="home"),
    path("exercise/", ExerciseView.as_view(), name="exercise"),
], "core")