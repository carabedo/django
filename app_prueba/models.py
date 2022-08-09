from django.db import models

class Participantes(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    mail = models.TextField(blank=True, null=True)
    team = models.TextField(blank=True, null=True)
    proyect_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participantes'

