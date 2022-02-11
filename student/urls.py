from django.urls import path
from student.views import list_apprentice

app_name = 'student'

urlpatterns = [
  path('list/', list_apprentice, name='list-apprentice'),
]


