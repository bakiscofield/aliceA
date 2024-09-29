from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import BookmakerSerializer
from api.models import Bookmaker

@api_view(["POST"])
def create_bookmaker(request):
    form = BookmakerSerializer(data=request.data)
    if form.is_valid():
        bookmaker_instance = form.save()                
        return Response(BookmakerSerializer(bookmaker_instance).data, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["PUT"])
def update_bookmaker(request, id):
    try:
        bookmaker = Bookmaker.objects.get(pk=id)
    except Bookmaker.DoesNotExist as bookmaker_not_found:
        return Response({"errors": bookmaker_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
    form = BookmakerSerializer(bookmaker, data=request.data)
    
    if form.is_valid():
        bookmaker_instance = form.save()
        return Response(bookmaker_instance, status=status.HTTP_201_CREATED)
    
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["DELETE"])
def delete_bookmaker(request, id):
    try:
        bookmaker = Bookmaker.objects.get(pk=id)
    except Bookmaker.DoesNotExist as bookmaker_not_found:
        return Response({"errors": bookmaker_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
    bookmaker.delete()
    
    return Response(bookmaker, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_bookmaker(request, id): 
    try:
        bookmaker = Bookmaker.objects.get(pk=id)
    except Bookmaker.DoesNotExist as bookmaker_not_found:
        return Response({"errors": bookmaker_not_found.__str__()}, status=status.HTTP_404_NOT_FOUND) 

    serializer = BookmakerSerializer(bookmaker).data
    
    return Response(serializer, status=status.HTTP_200_OK) 

@api_view(["GET"])
def get_bookmakers(request):   
    bookmakers = Bookmaker.objects.all()
    serializer = BookmakerSerializer(bookmakers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 

