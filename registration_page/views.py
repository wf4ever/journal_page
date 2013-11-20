from django.shortcuts import render_to_response
from forms import RegistrationForm

def home(request):
    return render_to_response('registration_page/login.html',{})

def authors(request):
    return render_to_response('registration_page/authors.html',{})

def title_and_abstract(request):
    return render_to_response('registration_page/title_and_abstract.html',{})

def thank_you(request):
    return render_to_response('registration_page/thank_you.html',{})

def details(request):
    return render_to_response('registration_page/details.html',{})

def sources(request):
    return render_to_response('registration_page/sources.html',{})