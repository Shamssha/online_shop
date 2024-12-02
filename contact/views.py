from django.http import HttpResponse
from django.shortcuts import render

from shop_settings.models import Ttings
from .models import Contact_us
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def contact_views(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('name')
        email = contact_form.cleaned_data.get('email')
        message = contact_form.cleaned_data.get('message')
        new_contact = Contact_us.objects.create(name=name, email=email, message=message)
        if new_contact is not None:
            messages.success(request, ("پیام شما موفقانه ارسال شد."))
        else:
            messages.error(request, ("مشکلی پیش آمد"))

    # contact = Contact_us.objects.all()
    context = {
        'contact_form':contact_form
    }
    return render(request,'contact_us.html', context)

def about(request):
    return render(request, "about.html")

