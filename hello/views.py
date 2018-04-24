from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .models import Greeting
from .forms import LeadForm

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'You are in!') 
        else:
            [messages.error(request, error) for error in form.errors]

    form = LeadForm()
    return render(request, 'index.html', {'form': form})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

