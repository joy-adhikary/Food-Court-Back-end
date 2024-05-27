from django.db import models
import uuid

class BaseClass(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    class Meta:
        abstract = True


# Create your models here.
class LoginModel(BaseClass):
    username = models.CharField(max_length= 255)
    password = models.CharField(max_length=255)

    # class Meta:
    #     ordering = ['created_at']
    
    def __str__(self):
        return self.username



class RegistrationModel(BaseClass):
    username = models.CharField(max_length= 255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    # class Meta:
    #     ordering = ['created_at']

    def __str__(self):
        return self.username


