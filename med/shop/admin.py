from django.contrib import admin

# Register your models here.

from .models import product
from .models import Contact
from .models import Customer

# Register your models here.


admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Customer)