from django.urls import path
from api.views import order_api_views
from api.views import client_api_views
from api.views import bookmaker_api_views
from api.views import employee_api_views
from api.views import codeparainage_api_views
from api.views import payment_method_api_views
from api.views import employee_payment_method_api_views

app_name = "api"

urlpatterns = [
    path('payment_methods', view=payment_method_api_views.get_payments_methode),
    path('payment_methods/create', view=payment_method_api_views.create_payement_methode),
    path('payment_methods/get/<int:id>', view=payment_method_api_views.get_payement_methode),
    path('payment_methods/update/<int:id>', view=payment_method_api_views.update_payement_methode),
    path('payment_methods/delete/<int:id>', view=payment_method_api_views.delete_payement_methode),
    
    path('employee_payement_methode_by_employee_and_bookmaker_and_payement_methode/<int:employee_id>/<int:bookmaker_id>/<int:payement_methode_id>', view=employee_payment_method_api_views.get_employee_payement_methode_by_employee_and_bookmaker_and_payement_methode),
    
    path('bookmakers', view=bookmaker_api_views.get_bookmakers),
    path('bookmakers/create', view=bookmaker_api_views.create_bookmaker),
    path('bookmakers/get/<int:id>', view=bookmaker_api_views.get_bookmaker),
    path('bookmakers/update/<int:id>', view=bookmaker_api_views.update_bookmaker),
    path('bookmakers/delete/<int:id>', view=bookmaker_api_views.delete_bookmaker),
    
    path('employee_payement_methodes', view=employee_payment_method_api_views.get_employee_payement_methodes),
    path('employee_payement_methodes/create', view=bookmaker_api_views.create_bookmaker),
    path('employee_payement_methodes/get/<int:id>', view=bookmaker_api_views.get_bookmaker),
    path('employee_payement_methodes/by/payement/methodes', view=employee_payment_method_api_views.get_employee_payement_methodes_by_payment_method),
    path('employee_payement_methodes/by/payement/methodes/<int:payment_method_id>', view=employee_payment_method_api_views.get_employee_payement_methodes_by_payment_method),
    path('employee_payement_methodes/delete/<int:id>', view=employee_payment_method_api_views.delete_employee_payement_methode),


    path('employees', view=employee_api_views.get_emplyees),
    path('employees/create', view=employee_api_views.create_employee),
    path('employees/get/<int:employee_id>', view=employee_api_views.get_employee),
    path('employees/update/<int:employee_id>', view=employee_api_views.update_employee),
    path('employees/enable/<int:employee_id>', view=employee_api_views.enable_employee),
    path('employees/disable/<int:employee_id>', view=employee_api_views.disable_employee),
    path('employees/delete/<int:employee_id>', view=employee_api_views.delete_employee),
    path('employees/filter/<int:bookmaker_id>/<int:payment_method_id>', view=employee_api_views.get_employees_by_bookmaker_and_payment_method),
    
    path('codeparainages', view=codeparainage_api_views.get_CodeParainages),
    path('codeparainages/create', view=codeparainage_api_views.create_codeparainage),
    path('codeparainages/get/<int:id>', view=codeparainage_api_views.get_codeparainage),
    path('codeparainages/update/<int:id>', view=codeparainage_api_views.update_codeparainage),
    path('codeparainages/delete/<int:id>', view=codeparainage_api_views.delete_codeparainage),
    
    path('clients', view=client_api_views.get_clients),
    path('clients/create', view=client_api_views.create_client),
    path('clients/get_or_create/<int:chat_id>', view=client_api_views.get_create_client),
    path('clients/get/<int:chat_id>', view=client_api_views.get_client),
    path('clients/update/<int:chat_id>', view=client_api_views.update_client),
    path('clients/delete/<int:chat_id>', view=client_api_views.delete_client),
    
    path('orders', view=order_api_views.get_orders),
    path('orders/create', view=order_api_views.create_order),
    path('orders/confirmed/<int:id>', view=order_api_views.confirm_order),
    path('orders/cancelled/<int:id>', view=order_api_views.cancel_order),   
]
