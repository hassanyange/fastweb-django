from django.db import models

# Create your models here

class Portifolio_detail(models.Model):
    project_name = models.CharField(max_length=255)
    project_image =models.ImageField(upload_to='img/')
    category = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    project_Date = models.DateField(auto_now_add=True)
    project_url = models.URLField(blank=True)
    project_Info = models.CharField(max_length=255)


    def __str__(self):
        return self.project_name
    
