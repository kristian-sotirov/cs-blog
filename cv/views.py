from django.shortcuts import render, get_object_or_404
from .models import Education, Project, Skill, Interest
from .forms import EducationForm, ProjectForm, SoftSkillForm, TechnicalSkillForm, InterestForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def cv_page(request):
	educations = Education.objects.all()
	projects = Project.objects.all()
	soft_skills = Skill.objects.filter(detail='Soft')
	langs = Skill.objects.filter(detail='Programming Language')
	systems = Skill.objects.filter(detail='Operating System')
	interests = Interest.objects.all()
	return render(request, 'cv/cv.html', {'educations':educations, 'projects':projects, 'soft_skills':soft_skills, 'langs':langs, 'systems':systems, 'interests':interests})

def education_page(request):
	educations = Education.objects.all()
	return render(request, 'cv/education.html', {'educations':educations})

@login_required		
def education_new(request):
	if request.method == 'POST':
		form = EducationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('education_page')
	else:
		form = EducationForm()	
	return render(request, 'cv/education_edit.html', {'form':form})

@login_required		
def education_edit(request, pk):
	education = get_object_or_404(Education, pk=pk)
	if request.method == "POST":
		form = EducationForm(request.POST, instance=education)
		if form.is_valid():
			form.save()
			return redirect('education_page')
	else:
		form = EducationForm(instance=education)
	return render(request, 'cv/education_edit.html', {'form':form})
	
def projects_page(request):
	projects = Project.objects.all()
	return render(request, 'cv/projects.html',{'projects':projects})	

@login_required		
def project_new(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('projects_page')
	else: 		
		form = ProjectForm()	
	return render(request, 'cv/project_edit.html', {'form':form})

@login_required		
def project_edit(request, pk):
	project = get_object_or_404(Project, pk=pk)
	if request.method =="POST":
		form = ProjectForm(request.POST, instance=project)
		if form.is_valid():
			form.save()
			return redirect('projects_page')
	else:
		form = ProjectForm(instance=project)
	return 	render(request, 'cv/project_edit.html', {'form':form})
	
def soft_skills_page(request):
	skills = Skill.objects.filter(detail='Soft')	
	return render(request, 'cv/soft_skills.html', {'skills':skills})

@login_required	
def soft_skill_new(request):
	if request.method == "POST":
		form = SoftSkillForm(request.POST)
		if form.is_valid():
			skill = form.save(commit=False)
			skill.detail = 'Soft'
			skill.save()
			return redirect('soft_skills_page')
	else:
		form = SoftSkillForm()
	return render(request, 'cv/soft_skill_edit.html', {'form':form})

@login_required		
def soft_skill_edit(request, pk):
	skill = get_object_or_404(Skill, pk=pk)
	if request.method == "POST":
		form = SoftSkillForm(request.POST, instance=skill)
		if form.is_valid():
			skill = form.save(commit=False)
			skill.detail = 'Soft'
			skill.save()
			return redirect('soft_skills_page')		
	else:
		form = SoftSkillForm(instance=skill)
	return render(request, 'cv/soft_skill_edit.html', {'form':form})
	
def technical_skills_page(request):
	langs = Skill.objects.filter(detail='Programming Language')
	systems = Skill.objects.filter(detail='Operating System')
	return render(request, 'cv/technical_skills.html', {'langs':langs, 'systems':systems})

@login_required		
def technical_skill_new(request):
	if request.method == "POST":
		form = TechnicalSkillForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('technical_skills_page')
	else:
		form = TechnicalSkillForm()		
	return render(request, 'cv/technical_skill_edit.html', {'form':form})
	
@login_required	
def technical_skill_edit(request, pk):
	skill = get_object_or_404(Skill, pk=pk)
	if request.method =="POST":
		form = TechnicalSkillForm(request.POST, instance = skill)
		if form.is_valid():
			form.save()
			return redirect('technical_skills_page')
	else:
		form = TechnicalSkillForm(instance=skill)
	return render(request, 'cv/technical_skill_edit.html', {'form':form})
	
def interests_page(request):
	interests = Interest.objects.all()
	return render(request, 'cv/interests.html', {'interests':interests})

@login_required	
def interest_new(request):
	if request.method =="POST":
		form = InterestForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('interests_page')
	else:
		form = InterestForm()
	return render(request, 'cv/interest_edit.html', {'form':form})

@login_required
def interest_edit(request, pk):
	interest = get_object_or_404(Interest, pk=pk)
	if request.method == "POST":
		form = InterestForm(request.POST, instance = interest)
		if form.is_valid():
			form.save()
			return redirect('interests_page')
	else:
		form = InterestForm(instance = interest)
	return render(request, 'cv/interest_edit.html', {'form':form})
				
		







	
	
	
