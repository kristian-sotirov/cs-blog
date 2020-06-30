from django.urls import path
from . import views

urlpatterns = [
	path('', views.cv_page, name='cv_page'),
	path('education/', views.education_page, name='education_page'),
	path('education/new/', views.education_new, name='education_new'),
	path('education/edit/<int:pk>/', views.education_edit, name='education_edit'),
	path('education/remove/<int:pk>/', views.education_remove, name='education_remove'),
	path('projects/', views.projects_page, name='projects_page'),
	path('projects/new/', views.project_new, name='project_new'),
	path('projects/edit/<int:pk>/', views.project_edit, name='project_edit'),
	path('projects/remove/<int:pk>/', views.project_remove, name='project_remove'),
	path('soft-skills/', views.soft_skills_page, name='soft_skills_page'),
	path('soft-skills/new/', views.soft_skill_new, name='soft_skill_new'),
	path('soft-skills/edit/<int:pk>/', views.soft_skill_edit, name='soft_skill_edit'),
	path('soft-skills/remove/<int:pk>/', views.soft_skill_remove, name='soft_skill_remove'),
	path('technical-skills/', views.technical_skills_page, name='technical_skills_page'),
	path('technical-skills/new/', views.technical_skill_new, name='technical_skill_new'),
	path('technical-skills/edit/<int:pk>/', views.technical_skill_edit, name='technical_skill_edit'),
	path('technical-skills/remove/<int:pk>/', views.technical_skill_remove , name='technical_skill_remove'),
	path('interests/', views.interests_page, name='interests_page'),
	path('interests/new/', views.interest_new, name='interest_new'),
	path('interests/edit/<int:pk>/', views.interest_edit, name='interest_edit'),
	path('interests/remove/<int:pk>/', views.interest_remove, name='interest_remove')	
]
