from django.db import models

# Create your models here.
class SocialLink(models.Model):
    platform=models.CharField(max_length=25)
    link=models.URLField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.platform