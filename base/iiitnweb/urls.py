from django.urls import path

from . import views

urlpatterns = [
		path('', views.home, name='home'),
        path('', views.Admission.admission, name='admission'),
        path('', views.Admission.undergraduate, name='admission'),
]

