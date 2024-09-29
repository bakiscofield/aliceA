from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import ClientSerializer
from api.models import Client

@api_view(["POST"])
def create_client(request):
    form = ClientSerializer(data=request.data)
    if form.is_valid():
        client_instance = form.save()                
        return Response(ClientSerializer(client_instance).data, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["POST"])
def get_create_client(request, chat_id):
    try:
        client = Client.objects.get(id_chat=chat_id)
        return Response(ClientSerializer(client).data, status=status.HTTP_200_OK)
    except Client.DoesNotExist as client_not_found:
        print(request.data)
        form = ClientSerializer(data=request.data)
        if form.is_valid():
            client_instance = form.save()                
            return Response(ClientSerializer(client_instance).data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)

@api_view(["PUT"])
def update_client(request, chat_id):
    try:
        client = Client.objects.get(chat_id=chat_id)
    except Client.DoesNotExist as client_not_found:
        return Response({"errors": client_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
    form = ClientSerializer(client, data=request.data)
    
    if form.is_valid():
        client_instance = form.save()
        return Response(client_instance, status=status.HTTP_201_CREATED)
    
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["DELETE"])
def delete_client(request, chat_id):
    try:
        client = Client.objects.get(chat_id=chat_id)
    except Client.DoesNotExist as client_not_found:
        return Response({"errors": client_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
    client.delete()
    
    return Response(client, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_client(request, chat_id): 
    try:
        client = Client.objects.get(id_chat=chat_id)
    except Client.DoesNotExist as client_not_found:
        return Response({"errors": client_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND) 

    serializer = ClientSerializer(client).data
    
    return Response(serializer, status=status.HTTP_200_OK) 

@api_view(["GET"])
def get_clients(request):
    clients = Client.objects.all()
    serializers = ClientSerializer(clients, many=True).data              
    return Response(serializers, status=status.HTTP_200_OK)




