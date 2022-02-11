from django.urls import path
from student.views import list_apprentice, save_assitance

app_name = 'student'

urlpatterns = [
  path('save/', save_assitance, name='save-assitance'),
  path('list/', list_apprentice, name='list-apprentice'),
]


