from django.contrib import admin

# Register your models here.
from .models import category,creator,product,altcategory

admin.site.register(category)
admin.site.register(altcategory)
admin.site.register(creator)
admin.site.register(product)
