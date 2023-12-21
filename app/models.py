from django.db import models

# Create your models here.
class Category(models.Model):
    CategoryName = models.CharField(max_length=20)
    
    def __str__(self):
        return self.CategoryName

class Notes(models.Model):
    Name = models.CharField(max_length=20)
    Description = models.TextField()
    
    categoryname = models.ForeignKey(Category,on_delete= models.CASCADE)
    
    def __str__(self):
        return self.Name   
