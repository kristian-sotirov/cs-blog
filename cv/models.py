from django.db import models

# Create your models here.

#class Career(models.Model):
#	pass

class Education(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	begin_date = models.CharField(max_length=4)
	end_date = models.CharField(max_length=7)
	
	def __str__(self):
		return self.name
	
class Project(models.Model):

	description = models.TextField(max_length=200)
	date = models.CharField(max_length=20)

	def __str__(self):
		return self.description
		
	
class Skill(models.Model):
	skill = models.CharField(max_length=30)
	detail = models.CharField(max_length=30)
	
	def __str__(self):
		return self.skill
		
class Interest(models.Model):
	interest = models.CharField(max_length=30)
	
	def __str__(self):
		return self.interest		
		
	
	

	
	
	
#class Interests(models.Model):
#	pass			
