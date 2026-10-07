from django.shortcuts import render,redirect
from .models import Application
from .forms import ApplicationForm



def application_list(request):

    applications=Application.objects.all()
    total_applications = applications.count()


    return render(
        request,"applications/application_list.html", {"applications": applications , "total_applications": total_applications})


def application_create(request):
    if request.method == "POST":
        form=ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("application_list")
        else: print(form.errors)
    else :
        form=ApplicationForm()
    return render(request,"applications/application_form.html",{"form":form})


def application_update(request,pk):
    application=Application.objects.get(id=pk)

    if request.method== "POST":
        form=ApplicationForm(request.POST,instance=application)
        if form.is_valid():
            form.save()
            return redirect("application_list")
    else:
        form=ApplicationForm(instance=application)
    return render(request,"applications/application_update.html",{"form":form})


def application_delete(request,pk):
    application=Application.objects.get(id=pk)

    if request.method == "POST":
        application.delete()
        return redirect("application_list")
    
    return render(
    request,
    "applications/application_confirm_delete.html",
    {"application": application})
        
