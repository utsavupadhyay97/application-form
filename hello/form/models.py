from django.db import models
from .validators import validate_file_extension
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    description = models.TextField()
    resume = models.FileField(upload_to='books/pdf',validators=[validate_file_extension] )
    
    def __str__(self):
        return self.name        