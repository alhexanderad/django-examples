from django.urls import path
from student.views import list_apprentice, save_assitance, get_into, record_assitance

app_name = 'student'

urlpatterns = [
  path('get_into/', get_into, name='get-into'),
  path('save/', save_assitance, name='save-assitance'),
  path('list/', list_apprentice, name='list-apprentice'),
  path('record/', record_assitance, name='record-assitance'),
]


