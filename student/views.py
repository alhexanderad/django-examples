from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_list_or_404
from student.models import Apprentice, Assistance
from datetime import datetime
from student.forms import AssistanceForm
from datetime import datetime


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
      return HttpResponseRedirect(reverse('student:list_apprentice',))
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


def list_apprentice(request):
  print("List de Aprendices")
  # if request.method == "POST":
  #   id = request.POST.getlist('assitance[]')
  #   print("Numero de id: ",id)
  #   return render(request, 'student/summary.html',)
    # id_asst = Assistance.objects.get(pk=id)
    # print("La salida es :", id_asst.exit_boolean)

  ass = Assistance.objects.all()

  context ={
    'title': "Lista",
    'ass' : ass,
  }
  return render(request, 'student/list.html', context)


def summary_assitance(request,pk,tm):
#Una persona cuenta con un DNI, debe ser registrado su ingreso y salida.
#Se realiza la busqueda la ultima vez que ingreso y que todavia no se registro su salida  
#Se tiene la busqueda pk de aprentice la entry_at
#Se debe de grabar summary
  app = Assistance.objects.filter(apprentice__id_app=pk,entry_at=tm,exit_boolean=False)
  time_now= datetime.now()
  
  print(time_now)
  ass_id = Assistance.objects.get(pk=app[0].id_ass)

  print(ass_id.id_ass)
  if request.method == "POST":
    ass_id.exit_boolean = True
    ass_id.exit_at = time_now
    ass_id.save(update_fields=['exit_boolean','exit_at'])
    print("se grabo")
    return HttpResponseRedirect(reverse('student:record_assitance',))
    

  #id_asst = Apprentice.objects.get(pk=int(ass_id.id_ass))

    # id_asst = Assistance.objects.get(pk=id)
    # print("La salida es :", id_asst.exit_boolean)
    # time_now = datetime.now()
    # print(time_now)
    
  print(ass_id)
  context ={
    'ass_id':ass_id,
    'title': 'Resumen',
    }
  return render(request, 'student/summary.html', context)


def record_assitance(request):

  asst = Assistance.objects.filter(entry_boolean=True, exit_boolean=True)
  days_times_total =[]
  for n in asst:
    app_1 = Assistance.objects.get(pk=n.id_ass)
    
    day_time_entry = app_1.entry_at.strftime('%y%m%d %H:%M:%S')
    day_time_exit = app_1.exit_at.strftime('%y%m%d %H:%M:%S')

    formato = '%y%m%d %H:%M:%S'
    day_time = datetime.strptime(day_time_exit, formato) - datetime.strptime(day_time_entry, formato)
    
    days_times_total.append(day_time)
    

  asst_time = zip(asst,days_times_total)
  context ={
    'title': "Historial",
    'asst_time' : asst_time,
  }
  return render(request, 'student/record.html', context)
