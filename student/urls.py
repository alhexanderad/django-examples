from django.urls import path
from student.views import list_apprentice, summary_assitance, get_into, record_assitance

app_name = 'student'

urlpatterns = [
  path('get_into/', get_into, name='get_into'),
  path('summary/<int:pk>/<str:tm>', summary_assitance, name='summary_assitance'),
  path('list/', list_apprentice, name='list_apprentice'),
  path('record/', record_assitance, name='record_assitance'),
]


