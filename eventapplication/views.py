from django.shortcuts import render
from .models import Participantlist
from django.core.exceptions import ValidationError

# Create your views here.

def home(request):
    context = {}
    return render(request, 'eventapplication/home.html', context)

def registration(request):
    context = {}
    if request.method == 'POST':
        p1 = Participantlist()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.age = request.POST.get('phone','00')
        p1.gender = request.POST.get('age','00')

        if len(Participantlist.objects.all()) > 15:
            return render(request, 'eventapplication/failed.html',context)
        else:
            p1.save()
            return render(request, 'eventapplication/success.html',context)

    if request.method == 'GET':
        context['name'] = '' 
        context['email address'] = '' 
        context['phone'] = '' 
        context['age'] = '' 

    return render(request, 'eventapplication/registration.html', context)  

def listofparticipants(request):
    context = {}

    context['participants'] = Participantlist.objects.all()

    return render(request, 'eventapplication/listofparticipants.html', context)    

def success(request):
    context = {}
    return render(request, 'eventapplication/success.html', context)

def failed(request):
    context = {}
    return render(request, 'eventapplication/failed.html', context)
