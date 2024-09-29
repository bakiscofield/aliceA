from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path('login', view=views.user_login, name='user_login'),
    path('logout', view=views.user_logout, name='user_logout'),
    
    path('generate_execl_data', view=views.generate_execl_data, name='generate_execl_data'),

    path('employees', view=views.employees_index, name='employees'),
    path('employees/create/or/edit', view=views.employees_create_or_edit, name='employees_create_or_edit'),
    path('employees/create/or/edit/<int:employee_id>', view=views.employees_create_or_edit, name='employees_create_or_edit'),
    
    path('caisses', view=views.employes_payements_index, name='caisses'),  
    path('caisses/create/or/edit', view=views.caisse_create_or_edit, name='caisse_create_or_edit'),
    path('caisses/create/or/edit/<int:caisse_id>', view=views.caisse_create_or_edit, name='caisse_create_or_edit'),
    
    
]
