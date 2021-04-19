from django.shortcuts import render
from .models import Job

# Create your views here.


def home(request):
    jobs = Job.objects.all()
    return render(request, 'my_app_jobs/home.html', {'jobs': jobs})
