from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.conf import settings
from dateutil import parser
from datetime import datetime, timedelta
from openpyxl import Workbook

from api.models import Client, Employee, EmployeePayementMethod, PayementMethod
from web.forms import EmployeeForm, EmployeePayementMethodForm


@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    if 'data_range' in request.GET:
        data_range = request.GET.get('data_range')
        if data_range:
            start_date_str, end_date_str = data_range.split(' - ')

            # Convertir les chaînes de date en objets datetime
            start_date = parser.parse(start_date_str)
            end_date = parser.parse(end_date_str)
    else:
        start_date = datetime.now()
        end_date = start_date + timedelta(days=7)
        
    meta_data, clients_by_week = Client.get_clients_count_by_interval(start_date, end_date)

    data = {
        'employes_count' :  len(Employee.objects.all()),
        'clients_count' :  len(Client.objects.all()),
        'meta_data' : meta_data,
        'clients_by_week': clients_by_week,
        'mois':  ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aoûte', 'septembre', 'octobre', 'novembre', 'décenbre'],
        'annees' : [i for i in range(2024, 2050)],
        'baki':"scofield",
    }
    
    print(data['mois'])
    print("baki")
    return render(request, "dashboard.html", data)

@login_required(login_url=settings.LOGIN_URL)
def generate_execl_data(request):
    if request.method == "POST":
        labels = str(request.POST.get('labels'))
        labels = labels.split(',')
        data = str(request.POST.get('data'))
        data = data.split(',')
        # Créer un classeur Excel
        # print(labels)
        # print(data)
        wb = Workbook()

        # Sélectionner la première feuille
        ws = wb.active

        # Ajouter des données à la feuille
        ws.append(["Date", "Nombre de clients"])
        for i in range(len(data)):
            ws.append([labels[i], data[i]])

        # Configurer la réponse HTTP
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=example.xlsx'

        # Écrire le contenu du classeur dans la réponse
        wb.save(response)

        return response


def user_login(request):
    if request.method == 'POST':
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        user = authenticate(request, username=contact, password=password)
        if user:
            login(request, user)
            return redirect('dashboard') 
        else:
            messages.error(request, 'Échec de la connexion. Veuillez vérifier votre contact et votre mot de passe.')
    
    return render(request, 'registration/login.html') 

@login_required(login_url=settings.LOGIN_URL)
def user_logout(request):
    logout(request)
    return redirect('web:user_login')

@login_required(login_url=settings.LOGIN_URL)
def employees_index(request):
    data = {
        "title" : "List des employés",
    }
    
    return render(request, "employees/index.html", context=data)

@login_required(login_url=settings.LOGIN_URL)
def employees_create_or_edit(request, employee_id=None):
    employee = Employee.objects.filter(id=employee_id).first()
    data = {}
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        form_is_valid = form.is_valid()
        if form_is_valid:
            employee = form.save()
            groups = request.POST.getlist('groups')
            print(groups)
            if groups:
                employee.user.groups.set(groups)
            data['message'] = f"Employe  ajouter avec succès !"
        data['form_is_valid'] = form_is_valid
    else:
        form = EmployeeForm(instance=employee) if employee is not None else EmployeeForm()
        if employee:
            form.initial['groups'] = employee.user.groups.all()
        
    context = {
        'form': form,
        'title' : "Ajouter un employé" if employee else "Mettre à jour un employé"
    }
    
    data['html_form'] = render_to_string(
        "employees/create_or_edit_partial.html",
        context,
        request=request,
    )
    return JsonResponse(data)

@login_required(login_url=settings.LOGIN_URL)
def employes_payements_index(request):
    payement_methods = PayementMethod.objects.all()
    data = {
        "title" : "Caisses",
        "payement_methods" : payement_methods
    }
    
    return render(request, "caisses/index.html", context=data)


@login_required(login_url=settings.LOGIN_URL)
def caisse_create_or_edit(request, caisse_id=None):
    caisse = EmployeePayementMethod.objects.filter(id=caisse_id).first()
    data = {}
    if request.method == 'POST':
        form = EmployeePayementMethodForm(request.POST, instance=caisse)
        form_is_valid = form.is_valid()
        if form_is_valid:
            form.save()
            data['message'] = f"Caisse  ajouter avec succès !"
        data['form_is_valid'] = form_is_valid
    else:
        form = EmployeePayementMethodForm(instance=caisse)
    
    context = {
        'form': form,
        'title' : "Ajouter une Caisse" if caisse else "Mettre à jour une Caisse"
    }
    
    data['html_form'] = render_to_string(
        "caisses/create_or_edit_partial.html",
        context,
        request=request,
    )
    
    return JsonResponse(data)
