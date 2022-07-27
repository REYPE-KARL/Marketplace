from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == "POST":
        name = request.POST.get('cname')
        email = request.POST.get('cemail')
        subject = request.POST.get('csubject')

        # vérifie si les valeurs sont vides
        if name == "" or email == "" or subject == "":
            if name == "":
                messages.error(request, 'Enter your name.', extra_tags='name')
            if email == "":
                messages.error(request, 'Enter your email.', extra_tags='email')
            if subject == "":
                messages.error(request, 'Enter your subject.', extra_tags='subject')
            return redirect('contact')

        contact = Contact()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        messages.success(request, 'Votre message a été envoyé. Merci de nous avoir contacter.')
        return redirect('contact')

    return render(request, 'contacts/contact.html')
