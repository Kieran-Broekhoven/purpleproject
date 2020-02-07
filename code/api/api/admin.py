from django.contrib import admin
from api import models


admin.site.register(models.Shelter)
admin.site.register(models.ItemRequest)
admin.site.register(models.HousingRequest)
admin.site.register(models.House)
