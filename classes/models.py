from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	name = models.CharField(max_length=120)
	dob = models.DateField()

	male = 'male'
	female = 'female'
	other = 'other'
	alien = 'alien'

	GENDER_CHOICES = [(male,"male"),(female,"female"),(other,"other"),(alien,"alien")]
	gender = models.CharField(max_length=120,choices=GENDER_CHOICES, default='alien')
	exam_grade = models.FloatField()
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
