from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import Portifolio_detail, Portifolio_section
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import  ContactForm


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

def myform(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            recipients = ["hassanyage@gmail.com"]

        try:
            send_mail(subject, message, from_email, recipients)
        except Exception as e:
           
            print(f"Error sending email: {e}")
            return HttpResponseRedirect("/error/")  # Redirect to an error page

        return HttpResponseRedirect("/thanks for contact us/")


