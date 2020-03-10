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


class Admission(TemplateView):
	def admission(self, request):
		return render(request, 'index.html')
	def undergraduate(self, request):
		return render(request, 'templates/index.html')
	# template_name =  templates['site']['admissions']['home']



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


