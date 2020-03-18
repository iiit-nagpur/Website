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
from .models import *

'''
To do
Add Contact class
'''


def home(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contacts.html')

class Home(TemplateView):
	def Abouts(request):
		#This page gives error if there are no objects of this model
		obj=About.objects.get(id=1)
		context={
			'title': obj.head,
			'description': obj.content
		}
		return render(request, 'Home/about.html', context)

	def Mission(request):
		return render(request, 'Home/mission.html')

	def Act(request):
		return render(request, 'Home/act.html')

	def UpcomingCampus(request):
		return render(request , 'Home/upcomingcampus.html')


class Admission(TemplateView):
	def Undergraduate(request):
		return render(request, 'Admission/undergraduate.html')

	def Postgraduate(request):
		return render(request, 'Admission/postgraduate.html')

	def PhD(request):
		return render(request, 'Admission/phd.html')

	def Fees(request):
		return render(request, 'Admission/fees.html')

	def FinancialAssistance(request):
		return render(request, 'Admission/financialassist.html')

	def Questions(request):
		obj = Faq.objects.all()
		return render(request, 'Admission/questions.html', {'faq': obj})

class People(TemplateView):
	def Faculty(request):
		object=Faculty.objects.all()
		return render(request, 'People/faculty.html',{'facdata':object})

	def AdjunctFaculty(request):
		object=Adjunctfac.objects.all()
		return render(request, 'People/adjunctfaculty.html',{'adjunctdata':object})

	def Staff(request):
		object=Staff.objects.all()
		return render(request, 'People/staff.html',{'staffdata':object})

	def Student(request):
		object=Student.objects.all()
		return render(request, 'People/student.html', {'studata':object})

	def Alumni(request):
		object=alumni.objects.all()
		return render(request, 'People/alumni.html', {'alumnidata':object})

class Academics(TemplateView):

	def Departments(request):
		object=departments.objects.all()
		return render(request, 'Academics/departments.html',{'depdata':object})

	def Programmes(request):
		object=programmes.objects.all()
		return render(request, 'Academics/programmes.html',{'prodata':object})

	def Convocation(request):
		return render(request, 'Academics/convocation.html')

	def Resources(request):
		return render(request, 'Academics/resources.html')

	def StudentVerification(request):
		return render(request, 'Academics/verification.html')

class Research(TemplateView):
	def Publications(request):
		return render(request, 'Research/publications.html')

	def ResearchAreas(request):
		return render(request, 'Research/research.html')

	def Events(request):
		return render(request, 'Research/events.html')

	def FellowshipAwards(request):
		return render(request, 'Research/awards.html')

class Placement(TemplateView):
	def Message(request):
		return render(request, 'Placement/message.html')

	def WhyRecruit(request):
		return render(request, 'Placement/whyrecruit.html')

	def Procedure(request):
		return render(request, 'Placement/procedure.html')

	def Statistics(request):
		return render(request, 'Placement/statistics.html')

	def Internships(request):
		return render(request, 'Placement/internships.html')

	def Recruiters(request):
		return render(request, 'Placement/recruiters.html')

	def Startups(request):
		return render(request, 'Placement/startups.html')

	def ContactTnP(request):
		return render(request, 'Placement/contacttnp.html')

class Careers(TemplateView):
	def FacultyRecruitment(request):
		return render(request, 'Careers/facrecruit.html')

	def StaffRecruitment(request):
		return render(request, 'Careers/staffrecruit.html')

class StudentAffairs(TemplateView):
	def EventsNews(request):
		return render(request, 'Student Affairs/events.html')

	def Facilities(request):
		return render(request, 'Student Affairs/facilities.html')

	def Hostels(request):
		return render(request, 'Student Affairs/hostels.html')

	def StudentClubs(request):
		return render(request, 'Student Affairs/studentclubs.html')

	def DisciplineGrievance(request):
		return render(request, 'Student Affairs/grievance.html')
