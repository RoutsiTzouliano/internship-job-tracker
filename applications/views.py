from django.shortcuts import render
from .models import Application



def application_list(request):

    applications=Application.objects.all()

    return render(
        request,"applications/application_list.html", {"applications": applications})
