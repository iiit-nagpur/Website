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
from .models import About

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

# def Abouts(request):
# 	obj=About.objects.get(id=1)
# 	context={
# 		'laud': obj.head,
# 		'pol': obj.content
# 	}
# 	return render(request, 'about.html', context)

class Home(TemplateView):
	def Abouts(request):
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
		return render(request, 'Admission/fess.html')

	def FinancialAssistance(request):
		return render(request, 'Admission/financial.html')

	def Questions(request):
		return render(request, 'Admission/questions.html')

class People(TemplateView):
	def Faculty(request):
		return render(request, 'People/faculty.html')

	def AdjunctFaculty(request):
		return render(request, 'People/adjuctfaculty.html')

	def Staff(request):
		return render(request, 'People/staff.html')

	def Btech(request):
		return render(request, 'People/btech.html')

	def Mtech(request):
		return render(request, 'People/mtech.html')

	def Phd(request):
		return render(request, 'People/phd.html')

	def Alumni(request):
		return render(request, 'People/alumni.html')

class Academics(TemplateView):
	def Rulebook(request):
		return render(request, 'Academics/rulebook.html')

	def Departments(request):
		return render(request, 'Academics/departments.html')

	def Programmes(request):
		return render(request, 'Academics/programs.html')

	def Convocation(request):
		return render(request, 'Academics/convocation.html')

	def Resources(request):
		return render(request, 'Academics/resources.html')

	def StudentVerification(request):
		return render(request, 'Academics/verification.html')

class Research(TemplateView):
	def Publications(request):
		return render(request, 'publications.html')

	def ResearchAreas(request):
		return render(request, 'research.html')

	def Events(request):
		return render(request, 'events.html')

	def FellowshipAwards(request):
		return render(request, 'awards.html')

class Placement(TemplateView):
	def Message(request):
		return render(request, 'message.html')

	def WhyRecruit(request):
		return render(request, 'whyrecruit.html')

	def Procedure(request):
		return render(request, 'procedure.html')

	def Statistics(request):
		return render(request, 'statistics.html')

	def Internships(request):
		return render(request, 'internships.html')

	def Recruiters(request):
		return render(request, 'recruiters.html')

	def Startups(request):
		return render(request, 'startups.html')

	def ContactTnP(request):
		return render(request, 'contacttnp.html')

class Careers(TemplateView):
	def FacultyRecruitment(request):
		return render(request, 'facrecruit.html')

	def StaffRecruitment(request):
		return render(request, 'staffrecruit.html')

class StudentAffairs(TemplateView):
	def EventsNews(request):
		return render(request, 'events.html')

	def Facilities(request):
		return render(request, 'facilities.html')

	def Hostels(request):
		return render(request, 'hostels.html')

	def StudentClubs(request):
		return render(request, 'studentclubs.html')

	def DisciplineGrievance(request):
		return render(request, 'grievance.html')







	# def get_context_data(*args, **kwargs):
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
