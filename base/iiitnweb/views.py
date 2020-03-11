from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect
import json

'''
To do
Add People/Community
Add Placement & Outreach
Add Student Affairs
Check Contact Section
Verify each function
'''


def home(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contacts.html')


class Home(TemplateView):
	def About(self,request):
		return render(request, 'about.html')

	def Mission(self,request):
		return render(request, 'mission.html')

	def Act(self,request):
		return rende(request, 'act.html')

	def UpcomingCampus(self,request):
		return render(request , 'upcomingcampus.html')


class Admission(TemplateView):
	def Undergraduate(self, request):
		return render(request, 'undergraduate.html')

	def Postgraduate(self, request):
		return render(request, 'postgraduate.html')

	def PhD(self,request):
		return render(request, 'phd.html')

	def Fees(self,request):
		return render(request, 'fess.html')

	def FinancialAssistance(self,request):
		return render(request, 'financial.html')

	def Questions(self,request):
		return render(request, 'questions.html')

class People(TemplateView):
	def Faculty(self,request):
		return render(request, 'faculty.html')

	def AdjunctFaculty(self,request):
		return render(request, 'adjuctfaculty.html')

	def Staff(self,request):
		return render(request, 'staff.html')

	def Btech(self,request):
		return render(request, 'btech.html')

	def Mtech(self,request):
		return render(request, 'mtech.html')

	def Phd(self,request):
		return render(request, 'phd.html')

	def Alumni(self,request):
		return render(request, 'alumni.html')

class Academics(TemplateView):
	def Rulebook(self,request):
		return render(request, 'rulebook.html')

	def Departments(self,request):
		return render(request, 'departments.html')

	def Programmes(self,request):
		return render(request, 'programs.html')

	def Convocation(self,request):
		return render(request, 'convocation.html')

	def Resources(self,request):
		return render(request, 'resources.html')

	def StudentVerification(self,request):
		return render(request, 'verification.html')

class Research(TemplateView):
	def Publications(self,request):
		return render(request, 'publications.html')

	def ResearchAreas(self,request):
		return render(request, 'research.html')

	def Events(self,request):
		return render(request, 'events.html')

	def FellowshipAwards(self,request):
		return render(request, 'awards.html')

class Placement(TemplateView):
	def Message(self,request):
		return render(request, 'message.html')

	def WhyRecruit(self,request):
		return render(request, 'whyrecruit.html')

	def Procedure(self,request):
		return render(request, 'procedure.html')

	def Statistics(self,request):
		return render(request, 'statistics.html')

	def Internships(self,request):
		return render(request, 'internships.html')

	def Recruiters(self,request):
		return render(request, 'recruiters.html')

	def Startups(self,request):
		return render(request, 'startups.html')

	def ContactTnP(self,request):
		return render(request, 'contacttnp.html')

class Careers(TemplateView):
	def FacultyRecruitment(self,request):
		return render(request, 'facrecruit.html')

	def StaffRecruitment(self,request):
		return render(request, 'staffrecruit.html')

class StudentAffairs(TemplateView):
	def EventsNews(self,request):
		return render(request, 'events.html')

	def Facilities(self,request):
		return render(request, 'facilities.html')

	def Hostels(self,request):
		return render(request, 'hostels.html')

	def StudentClubs(self,request):
		return render(request, 'studentclubs.html')

	def DisciplineGrievance(self,request):
		return render(request, 'grievance.html')







	# def get_context_data(self, *args, **kwargs):
	# 	context = super(Admissions,self).get_context_data(*args,**kwargs)
	# 	context['user_active']=False
	# 	if self.request.user.is_active:
	# 		context['user_active']=True
	# 		context['user']=self.request.user

	# 	context['title']=strings['admissions_title']
	# 	context['base'] = templates['base']['root']
	# 	context['mast'] = templates['build']['mast']
	# 	context['MAST_TEXT']="Admissions"
	# 	context['admissions_undergraduate'] = templates['site']['admissions']['undergraduate']
	# 	context['admissions_postgraduate'] = templates['site']['admissions']['postgraduate']
	# 	context['fee_structure'] = AdmissionsFeeStructure.objects.all()[0]
	# 	context['financial_assistance'] = AdmissionsFinancialAssistance.objects.order_by('order_no')
	# 	context['policy'] = Notes.objects.get(title='POLICY')
	# 	context['fee_mode_of_payment'] = AdmissionsFeeModeofPayment.objects.all()
	# 	context['fee_mode_of_payment_notes'] = Notes.objects.get(title='FEE')
	# 	return context
