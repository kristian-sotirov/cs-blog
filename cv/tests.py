from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from cv.models import Education, Project, Skill, Interest
from cv.views import cv_page

class CvPageTest(TestCase):
		
	def test_url_return_html(self):
		response = self.client.get('/cv/')
		self.assertTemplateUsed(response, 'cv/cv.html')
		
class EducationTest(TestCase):
		
	def test_url_return_education(self):
		response = self.client.get('/cv/education/')
		self.assertTemplateUsed(response, 'cv/education.html')
		
	def test_url_return_new_education(self):
		response = self.client.get('/cv/education/new/')
		self.assertTemplateUsed(response, 'cv/education_edit.html')
		
	def test_can_save_a_POST_request(self):
		self.client.post('/cv/education/new/', data={'name': 'A new institution', 'description': 'I like it here', 'begin_date': '2020', 'end_date': '2020'})
		response = self.client.get('/cv/education/')
		self.assertIn('A new institution', response.content.decode())
		self.assertIn('I like it here', response.content.decode())
		self.assertIn('2020', response.content.decode())
		self.assertTemplateUsed(response, 'cv/education.html')
		
class EducationModelTest(TestCase):

	def test_can_you_get_to_edit_education_after_created_one(self):
		first_school = Education()
		first_school.name = 'Testing School'
		first_school.description = 'I have studied in the Testing School where I had tests'
		first_school.begin_date = '2013'
		first_school.end_date = '2018'
		first_school.save()
		response = self.client.get('/cv/education/edit/1/')
		self.assertTemplateUsed(response, 'cv/education_edit.html')
		
	def test_saving_educations(self):
	
		#Create the first institution
		first_school = Education()
		first_school.name = 'Testing School'
		first_school.description = 'I have studied in the Testing School where I had tests'
		first_school.begin_date = '2013'
		first_school.end_date = '2018'
		first_school.save()
		
		#Create the second institution
		second_school = Education()
		second_school.name = 'Examing School'
		second_school.description = 'I have studied in the Examing School'
		second_school.begin_date = '2018'
		second_school.end_date = 'Present'
		second_school.save()
		
		#Check if all the objects are in the database
		saved_schools = Education.objects.all()
		self.assertEqual(saved_schools.count(), 2)
		
		
		first_saved_school = saved_schools[0]
		second_saved_school = saved_schools[1]
		
		#Check if the first school matches the description
		self.assertEqual(first_saved_school.name, 'Testing School')
		self.assertEqual(first_saved_school.description, 'I have studied in the Testing School where I had tests')
		self.assertEqual(first_saved_school.begin_date, '2013')
		self.assertEqual(first_saved_school.end_date, '2018')
		
		#Check if the second school matches the description
		self.assertEqual(second_saved_school.name, 'Examing School')
		self.assertEqual(second_saved_school.description, 'I have studied in the Examing School')
		self.assertEqual(second_saved_school.begin_date, '2018')
		self.assertEqual(second_saved_school.end_date, 'Present')
		
class ProjectPageTest(TestCase):
	
	def test_url_return_projects(self):
		response = self.client.get('/cv/projects/')		
		self.assertTemplateUsed(response, 'cv/projects.html')
	
	def test_url_return_new_projects(self):
		response = self.client.get('/cv/projects/new/')
		self.assertTemplateUsed(response, 'cv/project_edit.html')
			
	def test_can_save_a_POST_request(self):
		self.client.post('/cv/projects/new/', data={'description':'Test description', 'date':'16 April 1889'})
		response = self.client.get('/cv/projects/')
		self.assertIn('Test description', response.content.decode())
		self.assertIn('16 April 1889', response.content.decode())
		
class ProjectModelTest(TestCase):

	def test_can_you_get_to_edit_project_after_created_one(self):
		first_project = Project()
		first_project.description = 'This is a small first test'
		first_project.date = 'Random date'
		first_project.save()
		response = self.client.get('/cv/projects/edit/1/')
		self.assertTemplateUsed(response, 'cv/project_edit.html')
	
	def test_saving_projects(self):
	
		#Creating the first project
		first_project = Project()
		first_project.description = 'This is a small first test'
		first_project.date = 'Random date'
		first_project.save()
		
		#Creating the second project
		second_project = Project()
		second_project.description = 'This is another small but second test'
		second_project.date = 'Another random date'
		second_project.save()
		
		#Check whether the number of saved projects is the same
		saved_projects = Project.objects.all()
		self.assertEqual(2, saved_projects.count())
		
		#Extracting the first and the second projects from the safes
		first_saved_project = saved_projects[0]
		second_saved_project = saved_projects[1]
		
		#Check if the first project matches the description
		self.assertEqual(first_saved_project.description, 'This is a small first test')
		self.assertEqual(first_saved_project.date, 'Random date')
		
		#Check if the second project matches the description
		self.assertEqual(second_saved_project.description, 'This is another small but second test')
		self.assertEqual(second_saved_project.date, 'Another random date')
		
class SoftSkillsPageTest(TestCase):

	def test_url_return_soft_skills(self):
		response = self.client.get('/cv/soft-skills/')
		self.assertTemplateUsed(response, 'cv/soft_skills.html')
					
	def test_url_return_new_soft_skill(self):
		response = self.client.get('/cv/soft-skills/new/')
		self.assertTemplateUsed(response, 'cv/soft_skill_edit.html')
		
	def test_can_save_a_POST_request(self):
		self.client.post('/cv/soft-skills/new/', data={'skill':'Test skill'})
		response = self.client.get('/cv/soft-skills/')
		self.assertIn('Test skill',response.content.decode())
		
		
class SoftSkillsModelTest(TestCase):

	def test_can_you_get_to_edit_soft_skill_after_created_one(self):
		#Creating the first skill
		first_skill = Skill()
		first_skill.skill = 'Testing'
		first_skill.detail = 'Soft'
		first_skill.save()
		response = self.client.get('/cv/soft-skills/edit/1/')
		self.assertTemplateUsed(response, 'cv/soft_skill_edit.html')

	def test_saving_soft_skill(self):
	
		#Creating the first skill
		first_skill = Skill()
		first_skill.skill = 'Testing'
		first_skill.detail = 'Soft'
		first_skill.save()
		
		#Creating the second skill
		second_skill = Skill()
		second_skill.skill = 'Examing'
		second_skill.detail = 'Soft'
		second_skill.save()
		
		#Check whether the database has the same amount of entries as the created skills
		saved_skills = Skill.objects.all()
		self.assertEqual(saved_skills.count(), 2)
		
		#Extracting the entries
		saved_first_skill = saved_skills[0]
		saved_second_skill = saved_skills[1]
		
		#Checking whether the definition of the first saved skill matches with the created one
		self.assertEqual(saved_first_skill.skill, 'Testing')
		self.assertEqual(saved_first_skill.detail, 'Soft')
		
		#Checking whether the definition of the second saved skill matches with the created one
		self.assertEqual(saved_second_skill.skill, 'Examing')
		self.assertEqual(saved_first_skill.detail, saved_second_skill.detail)		
		
class TechnicalSkillsPageTest(TestCase):

	def test_url_return_technical_skills(self):
		response = self.client.get('/cv/technical-skills/')
		self.assertTemplateUsed(response, 'cv/technical_skills.html')
		
	def test_url_return_new_technical_skills(self):
		response = self.client.get('/cv/technical-skills/new/')
		self.assertTemplateUsed(response, 'cv/technical_skill_edit.html')
		
	def test_can_save_a_POST_request(self):
		self.client.post('/cv/technical-skills/new/', data={'skill':'C#', 'detail':'Programming Language'})	
		response = self.client.get('/cv/technical-skills/')
		self.assertIn('Programming', response.content.decode())
		self.assertIn('Language', response.content.decode())

class TechnicalSkillsModelTest(TestCase):

	def test_can_you_get_to_edit_soft_skill_after_created_one(self):
		#Creating the first skill
		first_skill = Skill()
		first_skill.skill = 'Testing'
		first_skill.detail = 'Programming Language'
		first_skill.save()
		response = self.client.get('/cv/technical-skills/edit/1/')
		self.assertTemplateUsed(response, 'cv/technical_skill_edit.html')
		
	#Here we don't have to test the creation of the skills themselves since that was checked in SoftSkillsModelTest
		
			
class InterestsPageTest(TestCase):
	
	def test_url_return_interests(self):
		response = self.client.get('/cv/interests/')
		self.assertTemplateUsed(response, 'cv/interests.html')
		
	def test_url_return_new_interest(self):
		response = self.client.get('/cv/interests/new/')
		self.assertTemplateUsed(response, 'cv/interest_edit.html')
		
	def test_can_save_a_POST_request(self):
		self.client.post('/cv/interests/new/', data={'interest':'Quantum Mechanics'})
		response = self.client.get('/cv/interests/')
		self.assertIn('Quantum Mechanics', response.content.decode())
				
class InterestsModelTest(TestCase):
	
	def test_can_you_get_to_edit_interest_after_created_one(self):
		first_interest = Interest()
		first_interest.interest = 'Testing'
		first_interest.save()
		response = self.client.get('/cv/interests/edit/1/')
		self.assertTemplateUsed(response, 'cv/interest_edit.html')
	
	
	def test_saving_interest(self):
	
		first_interest = Interest()
		first_interest.interest = 'Testing'
		first_interest.save()
		
		second_interest = Interest()
		second_interest.interest = 'Second testing'
		second_interest.save()
		
		saved_interests = Interest.objects.all()
		self.assertEqual(2, saved_interests.count())
		
		first_saved_interest = saved_interests[0]
		second_saved_interest = saved_interests[1]
		
		self.assertEqual(first_saved_interest.interest, 'Testing')
		self.assertEqual(second_saved_interest.interest, 'Second testing')
