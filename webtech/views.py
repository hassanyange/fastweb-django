from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage


# Create your views here.
def index(request):
    return render(request, 'index.html')

def portifolio(request):
    return render(request, 'portfolio-details.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Save the message to the database
        contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
        contact_message.save()
        messages.success(request, 'Your message has been sent!')
        return redirect('index')
    return render(request, 'index.html')