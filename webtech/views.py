from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import Portifolio_detail, Portifolio_section, Contact
from django.core.mail import send_mail
from django.http import HttpResponse



# Create your views here.
def index(request):
    portifolio_section = Portifolio_section.objects.all()
    return render(request, 'index.html', {'portifolio_section': portifolio_section})


def portifolio(request):
    portifolio = Portifolio_detail.objects.all()
    return render(request, 'portifolio-details.html', {'portifolio': portifolio})

# def portfolio_section(request):
#     portfolio_sections = Portifolio_section.objects.all()
#     return render(request, 'portfolio_section.html', {'portfolio_sections': portfolio_sections})

def myForm(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        query = Contact(name=name, email=email, subject=subject, message=message)
        query.save()
        messages.info(request,"Thanks for Reaching Us! we  will get you back soon....")
        return redirect("/contact")
    return render(request,'contact.html')


