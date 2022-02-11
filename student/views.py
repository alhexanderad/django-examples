import time
from cgi import print_environ
from multiprocessing import context
from django.shortcuts import render
from student.models import Apprentice, Assistance
from datetime import datetime

def list_apprentice(request):
  obj = Apprentice.objects.all()
  ass = Assistance.objects.all()
  
  app_1 = Assistance.objects.get(pk=4)
  
  print(app_1.entry_at)
  
  time_entry = app_1.entry_at.strftime('%H:%M')
  time_exit = app_1.exit_at.strftime('%H:%M')
  print("Entrada:", time_entry)
  print ("Salida: ",time_exit)
  formato = '%H:%M'
  tiempo = datetime.strptime(time_exit, formato) - datetime.strptime(time_entry, formato)
  #resultado = time_exit - time_entry

  context ={
    'title': "Lista",
    'obj': obj,
    'ass' : ass,
    'tiempo': tiempo,
  }
  return render(request, 'student/list.html', context)

def save_assitance(request):
  now = time.strftime("%H:%M:%S")
  print(now)
  context ={
    'time' : now,
    'title': 'Ingresar codigo de socio',
  }
  pass
  return render(request, 'student/save.html', context)