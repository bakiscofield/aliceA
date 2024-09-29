from django import forms
from api.models import Employee, Client, WithDrawalRequest,EmployeePayementMethod, ClientBookmaker, PayementMethod, Order
from django.contrib.auth.models import Group

class EmployeeForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), label="Roles",)
    class Meta:
        model = Employee
        fields = ['nom', 'prenom', 'contact', 'id_chat', 'country', 'username']

class EmployeePayementMethodForm(forms.ModelForm):
     class Meta:
        model = EmployeePayementMethod
        fields = [
            'id', 'code_agent', 'frais_depot', 
            'etablissement', 'rue', 'ville', 
            'employee', 'payment_method', 'bookmaker'
        ]

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'contact', 'code_parainage_depot', 'country']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}),
            'code_parainage_depot': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
        }

class WithDrawalRequestForm(forms.ModelForm):
    class Meta:
        model = WithDrawalRequest
        fields = ['client', 'montant_retrait', 'state']  # Retrait de 'message'
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'montant_retrait': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant'}),
            'state': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ClientBookmakerForm(forms.ModelForm):
    class Meta:
        model = ClientBookmaker
        fields = ['identifiant', 'client', 'bookmaker']
        widgets = {
            'identifiant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identifiant'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'bookmaker': forms.Select(attrs={'class': 'form-control'}),
        }

class PayementMethodForm(forms.ModelForm):
    class Meta:
        model = PayementMethod
        fields = ['nom_moyen', 'code_operation', 'mot_recharge', 'mot_retrait']
        widgets = {
            'nom_moyen': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du moyen'}),
            'code_operation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code opération'}),
            'mot_recharge': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mot de recharge'}),
            'mot_retrait': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mot de retrait'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'employee_payment_method', 'order_type', 'bookmaker_identifiant', 'montant', 'contact', 'code_parainage', 'state']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'employee_payment_method': forms.Select(attrs={'class': 'form-control'}),
            'order_type': forms.Select(attrs={'class': 'form-control'}),
            'bookmaker_identifiant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identifiant du bookmaker'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}),
            'code_parainage': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
        }
