from rest_framework import serializers
from .models import Programmer

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        #fields = ('fullmane', 'nickname')
        fields = '__all__'