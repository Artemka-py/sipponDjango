from django.db import models 
from django.shortcuts import reverse 

class Position(models.Model): 

  name = models.CharField(max_length = 50, verbose_name = 'Должность') 
  salary = models.FloatField(verbose_name = 'Зарплата') 

  class Meta: 
    verbose_name = "Должность" 
    verbose_name_plural = "Должности" 

  def __str__(self): 
    return self.name 

  def get_absolute_url(self): 
    return reverse("Position_detail", kwargs={"pk": self.pk}) 



class Empoyee(models.Model): 

  last_name = models.CharField(max_length = 50, verbose_name = 'Отчество') 
  first_name = models.CharField(max_length = 50, verbose_name = 'Имя')
  surname = models.CharField(max_length = 50, verbose_name = 'Фамилия') 
  birthday = models.DateField(verbose_name = 'Дата рождения') 
  fk_position = models.ForeignKey(Position, on_delete = models.DO_NOTHING, verbose_name = 'Должность') 

  class Meta: 
    verbose_name = "Сотрудник"
    verbose_name_plural = "Сотрудники"

  def __str__(self): 
    return '{} {} {}'.format(self.surname, self.first_name, self.last_name) 

  def get_absolute_url(self): 
    return reverse("_detail", kwargs={"pk": self.pk})