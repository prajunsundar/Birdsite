from django.db import models

class Birds(models.Model):
    name=models.CharField(max_length=200,unique=True)
    domain=models.CharField(max_length=200)
    slug = models.SlugField(default="", max_length=250, null=False)
    kingdom=models.CharField(max_length=200)
    details=models.TextField()
    image=models.ImageField(upload_to='images',blank=True)

    def __str__(self):
        return self.name
