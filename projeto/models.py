from django.db import models
from datetime import date 


class projeto(models.Model):
    titlle = models.CharField(verbose_name="Título",max_length=100, null=False, blank=False) #nome ou titulo da tarefa
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False) #criado quando, gera automatico 
    deadline = models.DateField(verbose_name="Data de entrega",null=False, blank=False) #data da entrega
    finished_at = models.DateField(null=True) #data q acabou 
    
    class Meta:
        ordering = ["deadline"]
        
    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
