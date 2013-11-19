from django.shortcuts import render_to_response
from forms import RegistrationForm

def home(request):
    return render_to_response('registration_page/login.html',{})

def authors(request):
    return render_to_response('registration_page/authors.html',{})

def authors(request):
    return render_to_response('registration_page/contribution_details.html',{})

def thank_you(request):
    return render_to_response('registration_page/thank_you.html',{})