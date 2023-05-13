from django.db import models

# Create your models here

class Portifolio_detail(models.Model):
    project_name = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to='img/', default='default/path/to/image.jpg')
    category = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    project_Date = models.DateField(auto_now_add=True)
    project_url = models.URLField(blank=True)
    project_Info = models.CharField(max_length=255)


    def __str__(self):
        return self.project_name
  

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.subject}"

