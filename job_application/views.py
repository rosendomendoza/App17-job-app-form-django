from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
from .admin import FormAdmin


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Fetch de user data
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            # Insert the user data into the database
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            # Send a email notification to the user
            message_body = (f"A new job application was submitted. Thank you, "
                            f"{first_name}")
            email_message = EmailMessage('Form submission confirmation',
                                         message_body, to=[email])
            email_message.send()

            # Send a success message to the user via webpage
            messages.success(request, "Form submitted successfully!")
    return render(request=request, template_name='index.html')


def about(request):
    return render(request=request, template_name='about.html')


def contact(request):
    return render(request=request, template_name='contact.html')


def admin():
    admin.site.register(Form, FormAdmin)
