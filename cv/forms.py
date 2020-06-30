from .models import Education, Project, Skill, Interest
from django import forms

class EducationForm(forms.ModelForm):

	class Meta:
		model = Education
		fields = ('name', 'description',  'begin_date', 'end_date')
		
class ProjectForm(forms.ModelForm):
	
	class Meta:
		model = Project
		fields = ('description', 'date')	
		
class SoftSkillForm(forms.ModelForm):

	class Meta:
		model = Skill
		fields = ('skill',)
		
class TechnicalSkillForm(forms.ModelForm):
	
	class Meta:
		model = Skill
		fields = ('skill', 'detail')
		
class InterestForm(forms.ModelForm):

	class Meta:
		model = Interest
		fields = ('interest',)				
