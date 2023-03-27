from django.db import models

# Create your models here.
class contactme(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.first_name
    
    