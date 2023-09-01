from rest_framework import serializers
from .models import UsersModels, StaffModels

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsersModels
        fields = ('name','last_name', 'age','access_recieved')

class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffModels
        fields = ('name', 'last_name', 'age','years_of_experience','salary_in_dollars')