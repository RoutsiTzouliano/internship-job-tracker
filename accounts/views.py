from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CandidateRegistrationForm
from .models import CandidateProfile
from django.db import transaction
# Create your views here

def registration(request):

    if request.method == 'POST':
        form = CandidateRegistrationForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                user = form.save()
                CandidateProfile.objects.create(user=user)
            login(request, user)
            return redirect('job_list')  
    else:
        form = CandidateRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})