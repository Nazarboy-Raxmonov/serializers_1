from django.db import models
from datetime import datetime

class UsersModels(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    access_recieved = models.DateField(default = datetime.now)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'User'

class StaffModels(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    years_of_experience =  models.IntegerField()
    salary_in_dollars = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'Staff'