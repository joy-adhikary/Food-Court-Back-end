from django.db import models

# Create your models here.
class LoginModel(models.Model):
    id = models.IntegerField(primary_key=True, auto_created= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    username = models.CharField(max_length= 255)
    password = models.CharField(max_length=255)

    # class Meta:
    #     ordering = ['created_at']
    
    def __str__(self):
        return self.username



class RegistrationModel(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    username = models.CharField(max_length= 255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    # class Meta:
    #     ordering = ['created_at']

    def __str__(self):
        return self.username


