from django.contrib import admin

from .models import RegistrationModel,LoginModel

# Register your models here.

admin.site.register(RegistrationModel)

admin.site.register(LoginModel)


# admin 5