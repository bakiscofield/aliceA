from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import EmployeePayementMethodSerializer
from api.models import EmployeePayementMethod, PayementMethod

@api_view(["POST"])
def create_employee_payement_methode(request):
    form = EmployeePayementMethodSerializer(data=request.data)
    if form.is_valid():
        payement_methode_instance = form.save()                
        return Response(PayementMethodeSerializer(payement_methode_instance).data, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["PUT"])
def update_employee_payement_methode(request, id):
    try:
        payement_methode = PayementMethode.objects.get(pk=id)
    except PayementMethode.DoesNotExist as payement_methode_not_found:
        return Response({"errors": payement_methode_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
    form = PayementMethodeSerializer(payement_methode, data=request.data)
    
    if form.is_valid():
        payement_methode_instance = form.save()
        return Response(payement_methode_instance, status=status.HTTP_201_CREATED)
    
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["DELETE"])
def delete_employee_payement_methode(request, id):
    content = {
        "title": "",
        "message" : "",
        "icon": "",
    }
    
    try:
        payement_methode = EmployeePayementMethod.objects.get(pk=id)
        payement_methode.delete()
    except EmployeePayementMethod.DoesNotExist as payement_methode_not_found:
        content['icon'] =  "error"
        content['title'] =  "Erreur"
        content['message'] =  payement_methode_not_found.__str__()
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    
    content['icon'] =  "success"
    content['title'] =  "Succès" 
    content['message'] = "Caisse supprimer avec succes"
    return Response(content, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_employee_payement_methode_by_employee_and_bookmaker_and_payement_methode(request, employee_id, bookmaker_id, payement_methode_id): 
    try:
        employee_payement_methode = EmployeePayementMethod.objects.get(employee__pk=employee_id, bookmaker__pk=bookmaker_id, payment_method__pk=payement_methode_id)
    except EmployeePayementMethod.DoesNotExist as employee_payement_methode_not_found:
        return Response({"errors": employee_payement_methode_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND) 
    serializer = EmployeePayementMethodSerializer(employee_payement_methode)
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(["GET"])
def get_employee_payement_methode(request, id): 
    try:
        employee_payement_methode = EmployeePayementMethod.objects.get(pk=id)
    except EmployeePayementMethod.DoesNotExist as employee_payement_methode_not_found:
        return Response({"errors": employee_payement_methode_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND) 
    serializer = EmployeePayementMethodSerializer(employee_payement_methode)
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(["GET"])
def get_employee_payement_methodes(request):  
    payement = PayementMethod.objects.all().first()
    employees_payement_methodes = EmployeePayementMethod.objects.all()
    serializer = EmployeePayementMethodSerializer(employees_payement_methodes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)     


@api_view(["GET"])
def get_employee_payement_methodes_by_payment_method(request, payment_method_id=None):
    if not payment_method_id:  
        payment_method_id = PayementMethod.objects.all().first().id
    employees_payement_methodes = EmployeePayementMethod.objects.filter(payment_method__id=payment_method_id)
    serializer = EmployeePayementMethodSerializer(employees_payement_methodes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)     
