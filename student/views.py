import time
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_list_or_404
from student.models import Apprentice, Assistance
from datetime import datetime
from student.forms import AssistanceForm
from datetime import datetime, timedelta


def list_apprentice(request):
  obj = Apprentice.objects.all()
  ass = Assistance.objects.all()
  
  app_1 = Assistance.objects.get(pk=2)
  
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

def get_into(request):

  en_test = datetime.timetuple(datetime.now())
  
  print(en_test)
    
  # if request.method == 'POST':
  #   asst = request.POST['apprentice']
  #   id_asst = Apprentice.objects.get(pk=asst)
    
  #   print(type(id_asst))
  #   en = True
  #   en_hour = timezone.localtime()
  #   ex = False
  #   ex_hour = timezone.localtime()
    
  #   print(en_hour)
    
  #   asst_save = Assistance(apprentice=id_asst , entry_boolean=en, entry_at=en_hour , exit_boolean=ex, exit_at=ex_hour)
  #   asst_save.save()
  
  if request.method == 'POST':
    asst = AssistanceForm(request.POST or None, request.FILES or None)
    id = request.POST['apprentice']
    id_asst = Apprentice.objects.get(pk=id)
    if asst.is_valid():
      data = asst.save(commit=False)
      data.apprentice = id_asst
      data.entry_boolean = True
      data.exit_boolean = False
      data.save()
      print("To save")
      return HttpResponseRedirect(reverse('student:list-apprentice',))
  else:
    forms = AssistanceForm(request.POST or None, request.FILES or None)
  # try

    
  #   if request.method == "POST":
  #     id = request.POST['idcode']
  #     print("Numero de id: ",id)
  #     userid = Apprentice.objects.get(pk=id)
  #     print("sisisiisis")
  #     


        # Apprentice.entry_boolean = request.POST['entry_boolean', True]


  # except Apprentice.DoesNotExist:
  #   print("No existe")

  context ={
    'title': 'Ingresar INGRESO',
    
    }

  return render(request, 'student/get_into.html', context)

def save_assitance(request):

  forms = AssistanceForm(request.POST or None, request.FILES or None)
  
  if forms.is_valid():
    instance = forms.save()

  try:
    app = Apprentice.objects.get(pk=10)
    print("Si es socio del Club")

  except Apprentice.DoesNotExist:
    print("No se encuentra en el Club")
  
  now = time.strftime("%H:%M:%S")
  print(now)

  context ={
    'time' : now,
    'title': 'Ingresar codigo de socio',
    'forms': forms,
    }
  return render(request, 'student/save.html', context)



