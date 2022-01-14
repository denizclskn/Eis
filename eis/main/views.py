from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.utils import html
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
from django.views.generic import View
from django.template.loader import get_template
from . import calculations
import xhtml2pdf.pisa as pisa
from .utils import render_to_pdf


@login_required(login_url="login")
def home(request):
    form = mapForm()
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = mapForm(request.POST)
            if form.is_valid():
                task = form.save()
                return redirect("reportQuestions", pk=task.id)
            else:
                messages.info(request, "Form hatalı")
    else:
        if request.method == "POST":
            return redirect("unreg")

    context ={
        "form":form,
        "user":user,
        "latitude": json.dumps(calculations.newLat),
        "longitude": json.dumps(calculations.newLng),
        "vs": json.dumps(calculations.newvs30),
    }
    return render(request, 'main/homePage.html', context)


@login_required(login_url="login")
def generatePDF(request, pk):
    context = {
        'pk': pk,
        }
    pdf = render_to_pdf('main/firstReport.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Report_%s.pdf" %(pk)
        content = "Inline; filename='%s" %(filename)
        response["Content-Disposition"] = content
        return response
    return HttpResponse("Not found")



def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        context = {
        }
        if request.method =="POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Kullanıcı adı veya şifre hatalı.")
                return render(request, 'main/login.html', context)
    
        return render(request, 'main/login.html', context)



def logoutUser(request):
    logout(request)
    return redirect("login")



def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = createUserForm()

        if request.method =="POST":
            form = createUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect("login")
        context = {
            "form":form
        }
        return render(request, 'main/register.html', context)


@login_required(login_url="login")
def firstReport(request, pk):
    if type(pk) is dict:
        val = pk["pk"]
        report = Report.objects.get(id=val)
    else:
        report = Report.objects.get(id=pk)
    context = {
        "report":report,
        "en": json.dumps(calculations.new_en),
        "boy": json.dumps(calculations.new_boy),
        "pga": json.dumps(calculations.new_pga10),
        "ss": json.dumps(calculations.new_ss10),
        "s1": json.dumps(calculations.new_s1_10),
        "pgv": json.dumps(calculations.new_pgv10),
    }
    return render(request, 'main/firstReport.html',context)


@login_required(login_url="login")
def createReport(request, pk):
   
    rep = Report.objects.get(id=pk)
    form = questionForm(instance=rep)
    context ={
        "form":form
    }
    if request.user.is_authenticated:
        if request.method == "POST":
            form = questionForm(request.POST, instance=rep)
            if form.is_valid():
                form.save()
            return redirect("firstReport", pk=pk)
    else:
         return redirect("firstReport")

    return render(request, 'main/reportQuestions.html',context)



@login_required(login_url="login")
def deleteReport(request, pk):
    report = Report.objects.get(id=pk)
    if request.method == "POST":
        report.delete()
        return redirect("/")
    context = {
        "report":report
    }
    return render(request, 'main/delete.html',context)



@login_required(login_url="login")
def myReports(request):
    #reports = Report.objects.get(userMail="mail")
    # userReports = reports.objects.all() 
    user = request.user
    username = user.username
    reports = Report.objects.filter(user=username)
    context = {
        "reports":reports,
    }
    return render(request, 'main/myReports.html', context)

