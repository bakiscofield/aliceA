from rest_framework import serializers

from api.models import Employee, CodeParainage, Client, Order, WithDrawalRequest, Bookmaker, PayementMethod, EmployeePayementMethod

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
           'id_chat', 'nom', 'prenom', 'contact', 'country'
        ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = instance.id
        representation['username'] = instance.username
        representation['enable'] = instance.user.is_active
        representation['groups'] = instance.user.groups.all().values_list('name', flat=True) if instance.id else ""
        representation['permissions'] = {}
        representation['create_at'] = instance.create_at
        return representation

class CodeParainageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeParainage
        fields = ['code', 'plafond_retrait', 'pourcentage_benefice', 'state']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id', 'id_chat', 'nom', 'prenom', 'contact', 'username', 'create_at',
            'code_parainage_depot', 'montant_parainage_depot', 'country'
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'client', 'employee_payment_method', 'order_type', 'reference_id', 
            'montant', 'code_parainage', 'bookmaker_identifiant', 'contact', 'state'
        ]

class OrderNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'reference_id', 
            'montant', 
            'bookmaker_identifiant',
            'contact',
        ]
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['type_transction'] = instance.order_type
        representation['bookmaker'] = instance.employee_payment_method.bookmaker
        representation['payment_method'] = instance.employee_payment_method.payment_method
        representation['username'] = instance.employee_payment_method.employee.username
        representation['contact'] = instance.client.contact
        return representation
    
class WithDrawalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithDrawalRequest
        fields = ['client', 'username', 'message', 'state', 'create_at', 'montant_retrait']

class BookmakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmaker
        fields = ['id', 'nom_bookmaker']

class PayementMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayementMethod
        fields = ['id', 'nom_moyen', 'code_operation', 'mot_recharge', 'mot_retrait']

class EmployeePayementMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePayementMethod
        fields = [
            'id', 'code_agent', 'frais_depot', 'frais_retrait', 
            'etablissement', 'rue', 'ville', 
            'employee', 'payment_method', 'bookmaker'
        ]
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['employee'] = instance.employee.fullname()
        representation['payment_method'] = instance.payment_method.nom_moyen
        representation['syntaxe'] = instance.get_syntaxe()
        return representation
    
    
