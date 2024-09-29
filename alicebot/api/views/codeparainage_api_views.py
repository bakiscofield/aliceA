from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import CodeParainageSerializer
from api.models import CodeParainage

@api_view(["POST"])
def create_codeparainage(request):
    form = CodeParainageSerializer(data=request.data)
    if form.is_valid():
        codeparainage_instance = form.save()                
        return Response(CodeParainageSerializer(codeparainage_instance).data, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["PUT"])
def update_codeparainage(request, id):
    try:
        codeparainage = CodeParainage.objects.get(pk=id)
    except CodeParainage.DoesNotExist as codeparainage_not_found:
        return Response({"errors": codeparainage_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
    form = CodeParainageSerializer(codeparainage, data=request.data)
    
    if form.is_valid():
        codeparainage_instance = form.save()
        return Response(codeparainage_instance, status=status.HTTP_201_CREATED)
    
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["DELETE"])
def delete_codeparainage(request, id):
    try:
        codeparainage = CodeParainage.objects.get(pk=id)
    except CodeParainage.DoesNotExist as codeparainage_not_found:
        return Response({"errors": codeparainage_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
    codeparainage.delete()
    
    return Response(codeparainage, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_codeparainage(request, id): 
    try:
        codeparainage = CodeParainage.objects.get(pk=id)
    except CodeParainage.DoesNotExist as codeparainage_not_found:
        return Response({"errors": codeparainage_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND) 

    serializer = CodeParainageSerializer(codeparainage).data
    
    return Response(serializer, status=status.HTTP_200_OK) 

@api_view(["GET"])
def get_CodeParainages(request):   
    codeparainage = CodeParainage.objects.all()
    serializer = CodeParainageSerializer(codeparainage, many=True)
    return Response(serializer, status=status.HTTP_200_OK) 

