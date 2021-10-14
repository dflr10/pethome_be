from django.contrib import admin
from .models.user import User
from .models.pet import Pet

# Register your models here.
admin.site.register(User)
admin.site.register(Pet)
