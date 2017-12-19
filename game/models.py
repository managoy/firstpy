from django.db import models

# Create your models here.

class question(models.Model):
	Q= models.CharField(max_length=255)
	A= models.CharField(max_length=255)


	def __str__(self):
		return self.Q

class answer(models.Model):
	q= models.ForeignKey(question, on_delete=models.CASCADE)
	#q=models.CharField(max_length=255)
	a= models.CharField(max_length=255)

	
	def __str__(self):
		return self.q


