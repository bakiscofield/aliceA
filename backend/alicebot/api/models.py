from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncDay
import base64

class Personne(models.Model):
    id_chat = models.CharField(max_length=255, unique=True)
    nom=models.CharField(max_length=50, default='', null=True)
    prenom=models.CharField(max_length=50, default='', null=True)
    contact=models.CharField(max_length=50, default='', null=True)
    create_at = models.DateField(auto_now=True, blank=True)
    username = models.CharField(max_length=50, blank=True, unique=True)
    COUNTRIES = [
        ("TG", "Togo")
    ]
    country = models.CharField(max_length=4, choices=COUNTRIES)
    
    class Meta:
        abstract=True
        
    def fullname(self):
        return f'{self.nom.upper()} {self.prenom.capitalize()}'
    
class Employee(Personne):
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    def save(self, *args, **kwargs):
        self.nom = self.nom.lower() if self.nom else ""
        self.prenom = self.prenom.lower() if self.prenom else ""
        if not self.id:
            self.username = f"CAISSIER{Employee.objects.count()+1}" # à modifier
            self.user=User.objects.create_user(username=str(self.contact),password='123456789')
        else:
            self.user.username = self.contact
            self.user.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nom + " "+ self.prenom
 
    def enable(self):
        self.user.is_active = True
        self.user.save()
    
    def disable(self):
        self.user.is_active = False
        self.user.save()
    
    def delete(self, *args, **kwargs):
        if self.user:
            self.user.delete()
        super().delete(*args, **kwargs)
     
class CodeParainage(models.Model):
    code = models.CharField(max_length=255, unique=True, blank=True)
    plafond_retrait = models.IntegerField(default=2000)
    pourcentage_benefice = models.FloatField(default=1)
    state = models.BooleanField(default=False, verbose_name="Activer le code")

class Client(Personne):   
    code_parainage_depot = models.OneToOneField(CodeParainage, on_delete=models.SET_NULL, null=True, blank=True)
    montant_parainage_depot = models.IntegerField(default=0, blank=True)
    
    def __str__(self):
        return self.nom + " "+ self.prenom
    
    def save(self, *args, **kwargs):
        if not self.id:
            nb = len(Client.objects.all())
            self.username = f'client {nb}'
        super().save(*args, **kwargs)
    
    def update_montant_parainage_depot(self, montant):
        self.montant_parainage_depot += montant*1/100
        self.save()
        
    def is_can_to_request_retrait(self):
        if self.code_parainage_depot:
            return self.montant_parainage_depot >= self.code_parainage_depot.plafond_retrait 
        return False
    
    def send_notification(self, montant_retrait, username):
        Notification.objects.create(client=self, montant_retrait=montant_retrait, username=username)
    
    def make_hash_id(self):
        return base64.b64encode(str(self.id).encode()).decode()
    
    @staticmethod
    def get_original_id(hash_id):
        return int(base64.b64decode(hash_id).decode())
    
    @classmethod
    def get_clients_count_by_interval(cls, start_date, end_date):
        queryset = cls.objects.annotate(
            day=TruncDay('create_at')
            ).values('day').annotate(count=Count('id')).values('day', 'count') 
        
        meta_data, data = [], []
        for item in queryset:
            meta_data.append(item['day'].strftime("%m/%d/%Y"))
            data.append(item['count'])
        #print(meta_data)
        return meta_data, data

class WithDrawalRequest(models.Model):
    """
    Demande de retrait 
    """
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=255)
    state = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=True)
    montant_retrait=models.IntegerField()
    
    def save(self, *args, **kwargs):
        self.message = f"Le client {self.client.full_name()} demande un retrait de {self.montant_retrait}"
        super().save()

class Bookmaker(models.Model):
    nom_bookmaker=models.CharField(max_length=500)
    
    def __str__(self):
        return self.nom_bookmaker 
       
class ClientBookmaker(models.Model):      
    identifiant=models.CharField(max_length=250, unique=True)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    bookmaker=models.ForeignKey(Bookmaker, on_delete=models.CASCADE)
    
    class Meta:
        unique_together=['client', 'bookmaker']
        
    def __str__(self):
        return f"{self.client}-{self.bookmaker}-{self.identifiant}"

class PayementMethod(models.Model):
    nom_moyen=models.CharField(max_length=500)
    code_operation=models.CharField(max_length=500)
    mot_recharge=models.CharField(max_length=20, null=True)
    mot_retrait=models.CharField(max_length=20, null=True)
    
    def save(self, *args, **kwargs):
        self.nom_moyen = self.nom_moyen.lower()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nom_moyen 
       
class EmployeePayementMethod(models.Model):      
    code_agent=models.IntegerField()
    frais_depot=models.IntegerField(default=50)
    frais_retrait=models.IntegerField(default=0, blank=True)
    etablissement=models.CharField(max_length=250)
    rue=models.CharField(max_length=100)
    ville=models.CharField(max_length=100)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    payment_method=models.ForeignKey(PayementMethod, on_delete=models.CASCADE)
    bookmaker=models.ForeignKey(Bookmaker, on_delete=models.CASCADE)
    
    class Meta:
        unique_together=['employee', 'payment_method', 'bookmaker']
    
    def get_syntaxe(self):
        return self.payment_method.code_operation.replace('{code_agent}', str(self.code_agent))
    
    def __str__(self):
        return str(self.code_agent) +" "+ "Ets: " +self.etablissement + " "+"rue: " +str(self.rue)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee_payment_method = models.ForeignKey(EmployeePayementMethod, on_delete=models.CASCADE)
    ORDER_TYPE_CHOICE = [
        ('DEPOT', 'DEPOT'),
        ('RETRAIT', 'RETRAIT')
    ]
    order_type = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICE) 
    # Pour évité que les clients n'envoye le même id
    bookmaker_identifiant = models.CharField(max_length=255) # ID 
    reference_id = models.CharField(max_length=255, unique=True)
    montant = models.IntegerField(null=True)
    contact = models.CharField(max_length=255)
    code_parainage = models.ForeignKey(CodeParainage, on_delete=models.SET_NULL,  null=True, blank=True)

    STATE_CHOICE = [
        ('COMMING', 'COMMING'),
        ('CONFIRMED', 'CONFIRMED'),
        ('CANCELLED', 'CANCELLED'),
    ]
    
    state = models.CharField(max_length=10, default=STATE_CHOICE[0][0], choices=STATE_CHOICE, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.identifiant = f"COMMADE {Order.objects.count()+1}"
            #self.save_client_bookmaker_id()
            
        super().save(*args, **kwargs)
        
        # if self.order_type == Order.STATE_CHOICE[1][1]:
        #     pass
        #     #self.update_montant()
        
    def save_client_bookmaker_id(self):
        if self.bookmaker_identifiant:
            ClientBookmaker.objects.get_or_create(
                    identifiant=self.bookmaker_identifiant, 
                    client=self.client,
                    bookmaker=self.employee_payment_method.bookmaker
                    )
    
    def get_employee_username(self):
        return self.employee_payment_method.employee.username
    
    def update_montant(self):
        if self.code_parainage and self.montant:
            self.code_parainage.client.update_montant_parainage_depot(self.montant)
    
    def confirm(self):
        self.state = Order.STATE_CHOICE[1][1]
        self.save()
    
    def cancel(self):
        self.state = Order.STATE_CHOICE[2][1]
        self.save()


        
