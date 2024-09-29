from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import OrderSerializer, OrderNotificationSerializer
from api.models import Order, Employee
import asyncio
from api.utils.bot_utils import send_notifications

@api_view(["POST"])
def create_order(request):
    form = OrderSerializer(data=request.data)
    try:
        form_is_valid = form.is_valid()
        if form_is_valid:
            order = form.save()
            
            admins_chat_ids = Employee.objects.filter(user__groups__name__in=["ADMIN", "SUPERADMIN"]).values_list('id_chat', flat=True)
            caissiers_chat_ids = Employee.objects.filter(employeepayementmethod__employee=order.employee_payment_method.employee).distinct().values_list('id_chat', flat=True)

            admins_chat_ids = list(admins_chat_ids)
            caissiers_chat_ids = list(caissiers_chat_ids)
            
            client_id = order.client.id_chat
            
            # admins_chat_ids = [5284977867]
            # caissiers_chat_ids = [5284977867]
            # client_id = 5284977867
            
            data = OrderNotificationSerializer(order).data
            asyncio.run(send_notifications(data, admins_chat_ids, caissiers_chat_ids, client_id))

            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 
    except Exception as e:
        return Response({"errors": e.__str__()}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def cancel_order(request, id):
    content = {'errors': '',}
    try:
        order = Order.objects.get(pk=id)
        order.cancel()
        content['message'] = 'Order cancelled successfully'
        content['data'] = order
        return Response(content, status=status.HTTP_201_CREATED)
    except Order.DoesNotExist as order_not_found:
        content['errors'] = order_not_found.__str__()
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        content['errors'] = e.__str__()
        return Response(content, status=status.HTTP_500_SERVER_ERROR) 
    
@api_view(["PUT"])
def confirm_order(request, id):
    content = {'errors': '',}
    try:
        order = Order.objects.get(pk=id)
        order.confirm()
        
        content['message'] = 'Order confirmed successfully'    
        content['data'] = order

        return Response(content, status=status.HTTP_201_CREATED)
    except Order.DoesNotExist as order_not_found:
        content['errors'] = order_not_found.__str__()
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        content['errors'] = e.__str__()
        return Response(content, status=status.HTTP_500_SERVER_ERROR) 
    
@api_view(["GET"])
def get_orders(request):   
    orders = Order.objects.all()
    serializers = OrderSerializer(orders, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK) 

@api_view(["GET"])
def get_orders_by_client(request, client_chat_id):   
    orders = Order.objects.filter(client__id_chat=client_chat_id)
    serializers = OrderSerializer(orders, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK) 



