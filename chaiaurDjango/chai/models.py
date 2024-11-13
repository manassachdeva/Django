from django.db import models
from django.utils import timezone
# Create your models here.
class chaivariety(models.Model):
    chaitype=[
        ('ML','Masala'),
        ('GR','Ginger'),
        ('KL','Kiwi'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="chais/")
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=chaitype)