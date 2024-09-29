from django.contrib import admin
from api.models import PayementMethod, Order

# Register your models here.
admin.site.register(Order)
admin.site.register(PayementMethod)