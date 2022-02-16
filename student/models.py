from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator

class Apprentice(models.Model):
  id_app = models.AutoField(primary_key=True)
  name = models.CharField(_("Nombres"), max_length=100, help_text="Debe de ingresar sus nombres completos")
  surname = models.CharField(_("Apellidos"), max_length=200, help_text="Ingrese sus apellidos completos")
  dni_regex = RegexValidator(regex=r'^\+?1?\d{8}', message = ("Debe de ingresar los 8 digitos de DNI"))
  dni_est = models.CharField( validators=[dni_regex], max_length=8, unique=True)
  created_at = models.DateTimeField(_("Creado"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Actualizado"), auto_now=True)
  
  def __str__(self):
    return str(self.name)
  
class Assistance(models.Model):
  id_ass = models.AutoField(primary_key=True)
  apprentice = models.ForeignKey(Apprentice, verbose_name=_("Aprendis"), on_delete=models.CASCADE)
  entry_boolean = models.BooleanField(default=False)
  entry_at = models.DateTimeField(_("Hora de Ingreso"), blank=True, null=True)
  exit_boolean = models.BooleanField(default=False)
  exit_at = models.DateTimeField(_("Hora de Salida"), blank=True, null=True)
  
  def __str__(self):
    return str(self.apprentice)