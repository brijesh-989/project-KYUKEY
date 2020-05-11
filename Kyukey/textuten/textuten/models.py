from django.db import migrations,models
from django.utils import timezone

class generate(models.Model):
    key = models.CharField(max_length=4)
    currentdate= models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.key)
    