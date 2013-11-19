from django.shortcuts import render_to_response

def home(request):
    return render_to_response('registration_page/home.html',{})