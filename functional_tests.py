#from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


#The story goes like this: I stumble upon this weird website which has the title "Introduction to programming" and the same is the header.

#I get curious and I decide to stalk this guy, and curiously enough he provided a "about me" link in the bottom
#(Note: this will be tested last/ the idea is just to provide a connection between my blog and my cv).



class visitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
		
	def helper_check_school(self, tag,  text):
		institutions = self.browser.find_elements_by_tag_name(tag)
		self.assertIn(text, [institution.text for institution in institutions])	
		
	def check_namespec_and_add_new_education(self, namespec, descriptionspec, beginspec, endspec):
		self.check_namespec_and_write('id_name', 'name', namespec)
		self.check_namespec_and_write('id_description', 'description', descriptionspec)
		self.check_namespec_and_write('id_begin_date', 'begin_date', beginspec)
		self.check_namespec_and_write('id_end_date', 'end_date', endspec)
		
	def check_namespec_and_add_new_project(self, descriptionspec, datespec):
		self.check_namespec_and_write('id_description', 'description', descriptionspec)
		self.check_namespec_and_write('id_date', 'date', datespec)	
		
	def check_namespec_and_add_new_soft_skill(self, skillspec):
		self.check_namespec_and_write('id_skill', 'skill', skillspec)
		
	def check_namespec_and_add_new_technical_skill(self, skillspec, detailspec):
		self.check_namespec_and_write('id_skill', 'skill', skillspec)
		self.check_namespec_and_write('id_detail', 'detail', detailspec)		
		
	def check_namespec_and_add_new_interest(self, namespec):
		self.check_namespec_and_write('id_interest', 'interest', namespec)	
		
	def check_namespec_and_write(self, idspec, namespec, text):
		inputbox = self.browser.find_element_by_id(idspec)
		nameText = inputbox.get_attribute('name')
		self.assertEqual(nameText, namespec)
		self.write_in_form(idspec, text)
		if namespec == 'end_date' or namespec == 'date' or namespec == 'skill' or namespec == 'detail' or namespec == 'interest':
			inputbox.send_keys(Keys.ENTER)			
		
	def write_in_form(self, idspec, text):
		inputbox = self.browser.find_element_by_id(idspec)
		inputbox.send_keys(text)
			
	def check_saved_education(self, namespec, descriptionspec, beginspec, endspec):
		names = self.browser.find_elements_by_tag_name('h3')
		specs = self.browser.find_elements_by_tag_name('p')
		self.assertIn(namespec, [name.text for name in names])
		self.assertIn(descriptionspec, [spec.text for spec in specs])
		self.assertIn(beginspec, [spec.text for spec in specs])
		self.assertIn(endspec, [spec.text for spec in specs])
		
	def check_saved_project(self, descriptionspec, datespec):
		descriptions = self.browser.find_elements_by_tag_name('h3')
		dates = self.browser.find_elements_by_tag_name('p')
		self.assertIn(descriptionspec, [description.text for description in descriptions])
		self.assertIn(datespec, [date.text for date in dates])
		
	def check_saved_soft_skill(self, skillspec):
		skills = self.browser.find_elements_by_tag_name('li')
		self.assertIn(skillspec, [skill.text for skill in skills])
		
	def check_saved_technical_skill(self, skillspec):
		skills = self.browser.find_elements_by_tag_name('li')
		self.assertIn(skillspec, [skill.text for skill in skills])
		
	def check_saved_interest(self, interestspec):
		interests = self.browser.find_elements_by_tag_name('li')
		self.assertIn(interestspec, [interest.text for interest in interests])
				
	def passed_test_view_the_education(self):
		#Probably the simpliest test:
		#I want to be able to visit the cv page just by clicking the home domain/cv url
		main_link = 'http://127.0.0.1:8000/cv/'
		self.browser.get(main_link)
		self.assertIn('Curriculum Vitae', self.browser.title)	
		
		#First lets check whether there exist a heading education.
		categories = self.browser.find_elements_by_tag_name('h2')
		self.assertIn('Education', [category.text for category in categories])
		
		#Now we test whether there is a link in the id of education and test it whether it leads to the right url.
		edu = self.browser.find_element_by_id('education')
		ed_link = edu.get_attribute('href')
		self.assertEqual(ed_link,'http://127.0.0.1:8000/cv/education/')		
		
		#Getting to the link we want. From here we want to create a new institution
		self.browser.get(ed_link)
		new_edu = self.browser.find_element_by_id('new_edu')
		new_ed_link = new_edu.get_attribute('href')
		self.assertEqual(new_ed_link, 'http://127.0.0.1:8000/cv/education/new/')
		self.browser.get(new_ed_link)	
		
		#Checking the name of every category and fill the form as well as submitting it!
		self.check_namespec_and_add_new_education('Testing School', 'I have studied in the Testing School where I had tests', '2013', '2018')	
				
		#Now we check whether the testing school is saved in the original education link
		self.browser.get(ed_link)
		self.check_saved_education('Testing School', 'I have studied in the Testing School where I had tests', '2013', '2018')
		
		#Now lets enter a new specification.
		self.browser.get(new_ed_link)
		self.check_namespec_and_add_new_education('Examing School', 'I have studied in the Examing School', '2018', 'Present')
		
		#And then we check whether both the specifications are saved
		self.browser.get(ed_link)
		self.check_saved_education('Testing School', 'I have studied in the Testing School where I had tests', '2013', '2018')
		self.check_saved_education('Examing School', 'I have studied in the Examing School', '2018', 'Present')
		
		#Let try to edit some of the content. Lets add a different description to the Examing school.
		
		#Firstly we get to the edit page of the exam.
		edit_exam = self.browser.find_element_by_id('edit_edu_47')
		edit_ed_link = edit_exam.get_attribute('href')
		self.browser.get(edit_ed_link)
		
		#Now lets change the description in the examing school.
		self.write_in_form('id_description', ' where I had exams')
		
		#saving the change!
		inputbox = self.browser.find_element_by_id('id_end_date')	
		inputbox.send_keys(Keys.ENTER)
		
		#Let's observe the change
		self.browser.get(ed_link)
		self.check_saved_education('Examing School', 'I have studied in the Examing School where I had exams', '2018', 'Present')
		
		
		#Now let's see whether all the changes are in the main page
		self.browser.get(main_link)
		self.check_saved_education('Testing School', 'I have studied in the Testing School where I had tests', '2013', '2018')
		self.check_saved_education('Examing School', 'I have studied in the Examing School where I had exams', '2018', 'Present')
	
	
	def passed_test_view_projects(self):
		
		#Go to the main page and see the heading that contains Projects
		main_link = 'http://127.0.0.1:8000/cv/'
		self.browser.get(main_link)		
		categories = self.browser.find_elements_by_tag_name('h2')
		self.assertIn('Projects', [category.text for category in categories])
		
		#Now let's see whether the link leads to the project url
		pro = self.browser.find_element_by_id('projects')
		pro_link = pro.get_attribute('href')
		self.assertEqual(pro_link,'http://127.0.0.1:8000/cv/projects/')
		
		#Go to the project link
		self.browser.get(pro_link)
		
		#Extract and check the link where you add a new project
		new_pro = self.browser.find_element_by_id('new_pro')
		new_pro_link = new_pro.get_attribute('href')
		self.assertEqual(new_pro_link,'http://127.0.0.1:8000/cv/projects/new/')
		self.browser.get(new_pro_link)
		
		#Now the form is going to be filled and the namespec will be checked. 
		self.check_namespec_and_add_new_project('Participated in a testing competition', 'October 2019')
		
		#Check whether the project is in the home page
		self.browser.get(pro_link)
		self.check_saved_project('Participated in a testing competition', 'October 2019')
		
		#Now enter a new specification
		self.browser.get(new_pro_link)
		self.check_namespec_and_add_new_project('Participated in a examing competition', 'December 2019')
		
		#Now check whether both specifications are in the projects
		self.browser.get(pro_link)
		self.check_saved_project('Participated in a testing competition', 'October 2019')
		self.check_saved_project('Participated in a examing competition', 'December 2019')
		
		#Here we are going to try and edit a project
		edit_pro = self.browser.find_element_by_id('edit_pro_24')
		edit_pro_link = edit_pro.get_attribute('href')
		self.browser.get(edit_pro_link)
		self.write_in_form('id_description',' and won it')
		inputbox = self.browser.find_element_by_id('id_date')
		inputbox.send_keys(Keys.ENTER)
		
		#This test will observe whether the specifications are preserved
		self.browser.get(pro_link)
		self.check_saved_project('Participated in a testing comptetition and won it', 'October 2019')
		
		#The final test will be whether the projects are shown in the main page
		self.browser.get(main_link)
		self.check_saved_project('Participated in a testing comptetition and won it', 'October 2019')
		self.check_saved_project('Participated in a examing competition', 'December 2019')
				
	def passed_test_view_soft_skills(self):
		
		#Firstly we try to find the page that leads to soft skills
		main_link = 'http://127.0.0.1:8000/cv/'
		self.browser.get(main_link)
		categories = self.browser.find_elements_by_tag_name('h2')
		self.assertIn('Soft Skills', [category.text for category in categories])
		
		#Check whether the link leads to the soft skills url
		skills = self.browser.find_element_by_id('soft-skills')
		skills_link = skills.get_attribute('href')	
		self.assertEqual(skills_link, 'http://127.0.0.1:8000/cv/soft-skills/')		
		
		#Now go to that link
		self.browser.get(skills_link)
		
		#Check and go to the link to add a new skill
		new_skill = self.browser.find_element_by_id('new-skill')
		new_skill_link = new_skill.get_attribute('href')
		self.assertEqual(new_skill_link, 'http://127.0.0.1:8000/cv/soft-skills/new/')
		self.browser.get(new_skill_link)
		
		self.check_namespec_and_add_new_soft_skill('Communication')
		
		#Now let's see whether the skill was saved
		self.browser.get(skills_link)
		self.check_saved_soft_skill('Communication')
		
		#Now let's add a new skill
		self.browser.get(new_skill_link)
		self.check_namespec_and_add_new_soft_skill('Work')
		
		#Let's check whether the second specification is saved
		self.browser.get(skills_link)
		self.check_saved_soft_skill('Communication')
		self.check_saved_soft_skill('Work')
		
		
		#From now on we try to edit the post and see whether the request is saved
		edit_skill = self.browser.find_element_by_id('edit_skill_22')
		edit_skill_link = edit_skill.get_attribute('href')
		self.browser.get(edit_skill_link)
		inputbox = self.browser.find_element_by_id('id_skill')
		inputbox.send_keys(' Ethics')
		inputbox.send_keys(Keys.ENTER)
		
		self.browser.get(skills_link)
		self.check_saved_soft_skill('Work Ethics')
		
		self.browser.get(main_link)
		self.check_saved_soft_skill('Communication')
		self.check_saved_soft_skill('Work Ethics')
		
	def passed_test_view_technical_skills(self):		
	
		#Check whether technical skills actually exist
		main_link = 'http://127.0.0.1:8000/cv/'
		self.browser.get(main_link)
		categories = self.browser.find_elements_by_tag_name('h2')
		self.assertIn('Technical Skills', [category.text for category in categories])
		
		#Check if the link leads to technical skills
		skills = self.browser.find_element_by_id('technical-skills')
		skills_link = skills.get_attribute('href')
		self.assertEqual(skills_link, 'http://127.0.0.1:8000/cv/technical-skills/')
		
		#Going to the link...
		self.browser.get(skills_link)
		
		#Firstly we check and then we are going to add a new technical skill
		new_skill = self.browser.find_element_by_id('new-skill')
		new_skill_link = new_skill.get_attribute('href')
		self.assertEqual(new_skill_link, 'http://127.0.0.1:8000/cv/technical-skills/new/')
		self.browser.get(new_skill_link)
		
		#Now check the namespec and add the technical skill to the database
		self.check_namespec_and_add_new_technical_skill('C', 'Programming Language')
		
		#Checking whether that is saved
		self.browser.get(skills_link)
		self.check_saved_technical_skill('C')
		
		#Writing a new skill and check whether the information is saved
		self.browser.get(new_skill_link)
		self.check_namespec_and_add_new_technical_skill('Linux', 'Operating System')
		self.browser.get(skills_link)
		self.check_saved_technical_skill('C')
		self.check_saved_technical_skill('Linux')
	
		#From here we are going to check whether we can edit a skill
		edit_skill = self.browser.find_element_by_id('edit_skill_41')
		edit_skill_link = edit_skill.get_attribute('href')
		self.browser.get(edit_skill_link)
		inputbox = self.browser.find_element_by_id('id_skill')
		inputbox.send_keys('++')
		inputbox = self.browser.find_element_by_id('id_detail')
		inputbox.send_keys(Keys.ENTER)
		
		self.browser.get(skills_link)
		self.check_saved_soft_skill('C++')
		
		self.browser.get(main_link)
		self.check_saved_soft_skill('C++')
		self.check_saved_soft_skill('Linux')
	
		
	def test_view_interests(self):
		
		#Checking whether interests actually exist
		main_link = 'http://127.0.0.1:8000/cv/'
		self.browser.get(main_link)
		categories = self.browser.find_elements_by_tag_name('h2')
		self.assertIn('Interests', [category.text for category in categories])
		
		#Check whether there is a link and if it leads to the interest page
		interests = self.browser.find_element_by_id('interests')
		interests_link = interests.get_attribute('href')
		self.assertEqual(interests_link, 'http://127.0.0.1:8000/cv/interests/')
		self.browser.get(interests_link)
		
		#Firstly we are going to add a new interests
		new_interest = self.browser.find_element_by_id('new-interest')
		new_interest_link = new_interest.get_attribute('href')
		self.assertEqual(new_interest_link, 'http://127.0.0.1:8000/cv/interests/new/')
		self.browser.get(new_interest_link)
		
		#Now we try to add the interest
		self.check_namespec_and_add_new_interest('Quantum')
		
		#Checking whether the interest is added
		self.browser.get(interests_link)
		self.check_saved_interest('Quantum')
		
		#Adding another interest and checking whether both are saved
		self.browser.get(new_interest_link)
		self.check_namespec_and_add_new_interest('Travelling')
		self.browser.get(interests_link)
		self.check_saved_interest('Quantum')
		self.check_saved_interest('Travelling')
		
		edit_interest = self.browser.find_element_by_id('edit_interest_10')
		edit_interest_link = edit_interest.get_attribute('href')
		self.browser.get(edit_interest_link)
		inputbox = self.browser.find_element_by_id('id_interest')
		inputbox.send_keys(' Mechanics')
		inputbox.send_keys(Keys.ENTER)
		
		self.browser.get(interests_link)
		self.check_saved_interest('Quantum Mechanics')
		
		self.browser.get(main_link)
		self.check_saved_interest('Quantum Mechanics')
		self.check_saved_interest('Travelling')
		
		
		
		
		
		
		self.fail('Not ready!!!')
		
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')		
					
