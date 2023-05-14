from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from .models import Portifolio_detail,Portifolio_section, Contact
from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def portifolio(request):
    portifolio = Portifolio_detail.objects.all()
    return render(request, 'portfolio-details.html')

def portifolio_section(request):
    portifolio_section = Portifolio_section.objects.all()


    return render(request, 'index.html')



def contact(request):
    if request.method == 'POST':
            contact = Contact()
            name = request.POST.get( 'name')
            email = request.POST.get( 'email')
            subject = request.POST.get( 'subject')
            message = request.POST.get( 'message')
            contact.name = name
            contact.email = email
            contact.subject = subject
            contact.message = message
            contact.save()
            return HttpResponse('Thanks for contact us !')
                     
    return render(request, 'index.html')
    