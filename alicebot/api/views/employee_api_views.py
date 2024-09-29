from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import EmployeeSerializer
from api.models import Employee, Bookmaker, PayementMethod
from api.utils.other_classes import ResponseMessage

@api_view(["POST"])
def create_employee(request):
    try:
        form = EmployeeSerializer(data=request.data)
        if form.is_valid():
            employee_instance = form.save()        
            response = ResponseMessage.makeSuccessInstanceResponseMessage(message=f"Employé {employee_instance.nom} à été enregisté avec success")
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 
    except Exception as e:
        response = ResponseMessage.makeErrorInstanceResponseMessage(message="Erreur du server veuillez contacter les developpeurs")
        print(e)
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
def update_employee(request, employee_id): 
    try:
        employee = Employee.objects.get(pk=employee_id)
        form = EmployeeSerializer(employee, data=request.data)
        if form.is_valid():
            employee_instance = form.save()                
            return Response(EmployeeSerializer(employee_instance).data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 
    except Employee.DoesNotExist as employee_not_found:
        return Response({"errors": employee_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"errors": e.__str__()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def enable_employee(request, employee_id): 
    try:
        employee = Employee.objects.get(pk=employee_id)
        employee.enable()
        response = ResponseMessage.makeSuccessInstanceResponseMessage(message=f"Employé {employee.nom} à été activé avec success")
        return Response(response.tojson(), status=status.HTTP_200_OK)
    except Employee.DoesNotExist as employee_not_found:
        return Response({"errors": employee_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND) 

@api_view(["PUT"])
def disable_employee(request, employee_id): 
    try:
        employee = Employee.objects.get(pk=employee_id)
        employee.disable()
        response = ResponseMessage.makeSuccessInstanceResponseMessage(message=f"Employé {employee.nom} à été activé avec success")
        return Response(response.tojson(), status=status.HTTP_200_OK)
    except Employee.DoesNotExist as employee_not_found:
        return Response({"errors": employee_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND) 
                  
@api_view(["DELETE"])
def delete_employee(request, employee_id): 
    content = {
        "title": "",
        "message" : "",
        "icon": "",
    }
    try:
        employee = Employee.objects.get(pk=employee_id)
        employee.delete()
    except Employee.DoesNotExist as employee_not_found:
        content['icon'] =  "error"
        content['title'] =  "Erreur"
        content['message'] =  employee_not_found.__str__()
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    content['icon'] =  "success"
    content['title'] =  "Succès" 
    content['message'] = "Employé supprimer avec succes"
    return Response(content, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_employee(request, employee_id): 
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist as employee_not_found:
        return Response({"errors": employee_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND) 

    serializer = EmployeeSerializer(employee).data
    
    return Response(serializer, status=status.HTTP_200_OK) 

@api_view(["GET"])
def get_emplyees(request):   
    employees = Employee.objects.all()
    serializers = EmployeeSerializer(employees, many=True).data
    return Response(serializers, status=status.HTTP_200_OK) 

@api_view(["GET"])
def get_employees_by_bookmaker_and_payment_method(request, bookmaker_id, payment_method_id):  
    try:
        payment_method = PayementMethod.objects.get(pk=payment_method_id)
        employees = Employee.objects.filter(employeepayementmethod__bookmaker__id=bookmaker_id, employeepayementmethod__payment_method=payment_method)
    except PayementMethod.DoesNotExist as payment_method_not_found:
        print(payment_method_not_found)
        return Response({"errors" :  payment_method_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EmployeeSerializer(employees, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK) 
