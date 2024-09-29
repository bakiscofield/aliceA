from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import WithDrawalRequestSerializer
from api.models import WithDrawalRequest

@api_view(["POST"])
def create_withdrawalrequest(request):
    form = WithDrawalRequestSerializer(data=request.data)
    if form.is_valid():
        withdrawalrequest_instance = form.save()                
        return Response(WithDrawalRequestSerializer(withdrawalrequest_instance).data, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["PUT"])
def update_withdrawalrequest(request, id):
    try:
        withdrawalrequest = WithDrawalRequest.objects.get(pk=id)
    except WithDrawalRequest.DoesNotExist as withdrawalrequest_not_found:
        return Response({"errors": withdrawalrequest_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
    form = WithDrawalRequestSerializer(withdrawalrequest, data=request.data)
    
    if form.is_valid():
        withdrawalrequest_instance = form.save()
        return Response(withdrawalrequest_instance, status=status.HTTP_201_CREATED)
    
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["DELETE"])
def delete_withdrawalrequest(request, id):
    try:
        withdrawalrequest = WithDrawalRequest.objects.get(pk=id)
    except WithDrawalRequest.DoesNotExist as withdrawalrequest_not_found:
        return Response({"errors": withdrawalrequest_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
    withdrawalrequest.delete()
    
    return Response(withdrawalrequest, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_withdrawalrequest(request, id): 
    try:
        withdrawalrequest = WithDrawalRequest.objects.get(pk=id)
    except WithDrawalRequest.DoesNotExist as withdrawalrequest_not_found:
        return Response({"errors": withdrawalrequest_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND) 

    serializer = WithDrawalRequestSerializer(withdrawalrequest).data
    
    return Response(serializer, status=status.HTTP_200_OK) 

@api_view(["GET"])
def get_withdrawalrequests(request):   
    withdrawalrequest = WithDrawalRequest.objects.all()
    serializer = WithDrawalRequestSerializer(withdrawalrequest, many=True)
    return Response(serializer, status=status.HTTP_200_OK) 

