from api.models import Order


def change_order_state(confirm: bool, order_id: int):
    order = Order.objects.filter(pk=order_id).first()
    if order:
        if confirm:
            order.confirm()
        else:
            order.cancel()
            
    return order
