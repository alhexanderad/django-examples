from django.db import models
from django.utils.translation import gettext as _

class Apprentice(models.Model):
  id_app = models.AutoField(primary_key=True)
  name = models.CharField(_("Nombres"), max_length=100, help_text="Debe de ingresar sus nombres completos")
  surname = models.CharField(_("Apellidos"), max_length=200, help_text="Ingrese sus apellidos completos")
  created_at = models.DateTimeField(_("Creado"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Actualizado"), auto_now=True)
  
  def __str__(self):
    return str(self.name)
  
class Assistance(models.Model):
  id_ass = models.AutoField(primary_key=True)
  apprentice = models.ForeignKey(Apprentice, verbose_name=_("Aprendis"), on_delete=models.CASCADE)
  entry_at = models.DateTimeField(_("Hora de Ingreso"), blank=True,null=True)
  exit_at = models.DateTimeField(_("Hora de Salida"), blank=True,null=True)
  
  def __str__(self):
    return str(self.apprentice)