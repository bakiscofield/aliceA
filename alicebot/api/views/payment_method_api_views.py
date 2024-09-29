from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import PayementMethodSerializer
from api.models import PayementMethod


@api_view(["POST"])
def create_payement_methode(request):
    form = PayementMethodSerializer(data=request.data)
    if form.is_valid():
        payement_methode_instance = form.save()                
        return Response(PayementMethodSerializer(payement_methode_instance).data, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["PUT"])
def update_payement_methode(request, id):
    try:
        payement_methode = PayementMethod.objects.get(pk=id)
    except PayementMethod.DoesNotExist as payement_methode_not_found:
        return Response({"errors": payement_methode_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
    form = PayementMethodSerializer(payement_methode, data=request.data)
    
    if form.is_valid():
        payement_methode_instance = form.save()
        return Response(payement_methode_instance, status=status.HTTP_201_CREATED)
    
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["DELETE"])
def delete_payement_methode(request, id):
    try:
        payement_methode = PayementMethod.objects.get(pk=id)
    except PayementMethod.DoesNotExist as payement_methode_not_found:
        return Response({"errors": payement_methode_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
    payement_methode.delete()
    
    return Response(payement_methode, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_payement_methode(request, id): 
    try:
        payement_methode = PayementMethod.objects.get(pk=id)
    except PayementMethod.DoesNotExist as payement_methode_not_found:
        return Response({"errors": payement_methode_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND) 

    serializer = PayementMethodSerializer(payement_methode).data
    
    return Response(serializer, status=status.HTTP_200_OK) 

@api_view(["GET"])
def get_payments_methode(request):  
    payements_methode = PayementMethod.objects.all()
    serializer = PayementMethodSerializer(payements_methode, many=True).data
    return Response(serializer, status=status.HTTP_200_OK) 
