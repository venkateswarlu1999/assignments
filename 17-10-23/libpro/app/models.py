from django.db import models

# Create your models here.
class author(models.Model):
    name=models.CharField(max_length=100)
    
class lbbooks(models.Model):
    tittle=models.CharField(max_length=50),
    author_id=models.ForeignKey(author, on_delete=models.CASCADE)