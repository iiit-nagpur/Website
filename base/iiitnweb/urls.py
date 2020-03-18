from django.urls import path
from . import views

# lol = views.Home()

urlpatterns = [
		path('', views.home, name='home'),
		path('contact/', views.contact, name='contact'),
		path('undergraduate/', views.Admission.Undergraduate, name='undergraduate'),
		path('postgraduate/', views.Admission.Postgraduate, name='postgraduate'),
		path('phd/', views.Admission.PhD, name='phd'),
		path('fees/', views.Admission.Fees, name='fees'),
		path('financialassist/', views.Admission.FinancialAssistance, name='financialassist'),
		path('questions/', views.Admission.Questions, name='question'),
		path('about/', views.Home.Abouts, name='about'),
        path('mission/', views.Home.Mission, name='mission'),
		path('', views.Home.UpcomingCampus, name='campus'),
		path('faculty/', views.People.Faculty, name='facult'),
		path('adjunctfaculty/', views.People.AdjunctFaculty, name='adjunctfac'),
		path('staff/', views.People.Staff, name='staf'),
		path('student/', views.People.Student, name='stud'),
		path('alumni/', views.People.Alumni, name='alumn'),
		path('departments/', views.Academics.Departments, name='department'),
		path('program/', views.Academics.Programmes, name='program'),
		path('convocation/', views.Academics.Convocation, name='convocation'),
		path('resources/', views.Academics.Resources, name='resources'),
		path('verification/', views.Academics.StudentVerification, name='verification'),
		path('publications/', views.Research.Publications, name='publications'),
		path('researchareas/', views.Research.ResearchAreas, name='researchareas'),
		path('events/', views.Research.Events, name='events'),
		path('awards/', views.Research.FellowshipAwards, name='awards'),
		path('message/', views.Placement.Message, name='message'),
		path('whyrecruit/', views.Placement.WhyRecruit, name='whyrecruit'),
		path('procedure/', views.Placement.Procedure, name='procedure'),
		path('statistics/', views.Placement.Statistics, name='statistics'),
		path('internships/', views.Placement.Internships, name='internships'),
		path('recruiters/', views.Placement.Recruiters, name='recruiters'),
		path('startups/', views.Placement.Startups, name='startups'),
		path('contactTnp/', views.Placement.ContactTnP, name='contactTnp'),
		path('facrecruit/', views.Careers.FacultyRecruitment, name='facrecruit'),
		path('staffrecruit/', views.Careers.StaffRecruitment, name='staffrecruit'),
		path('eventnews/', views.StudentAffairs.EventsNews, name='eventnews'),
		path('facilities/', views.StudentAffairs.Facilities, name='facilities'),
		path('hostels/', views.StudentAffairs.Hostels, name='hostels'),
		path('studentclubs/', views.StudentAffairs.StudentClubs, name='studentclubs'),
		path('grievance/', views.StudentAffairs.DisciplineGrievance, name='grievance'),
]
