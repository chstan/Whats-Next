from django.db import models

class Task(models.Model):
	title = models.CharField(max_length = 60)
	description = models.CharField()
	urgency = models.IntegerField()
	due_date = models.DateField()


	owner = models.ForeignKey(User)