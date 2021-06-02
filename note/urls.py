from django.urls import path

from . import views

app_name = 'note'

urlpatterns = [
    path('', views.NotesView.start_page),
]
