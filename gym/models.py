from django.db import models

# Create your models here.
class GYM_details(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False)
    m_number=models.CharField(max_length=10,blank=False,null=False)

    age=models.IntegerField()
    height=models.IntegerField()
    weight=models.IntegerField()
    plan=models.CharField(max_length=25,blank=False,null=False)
    
    gender=models.CharField(max_length=25,blank=False,null=False)
    
    
    def __str__(self):
        return self.name