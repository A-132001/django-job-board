# get data from model ----> json

from rest_framework import serializers
from .models import Job,Applyers

class SerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class SerializerApplyersModel(serializers.ModelSerializer):
    class Meta:
        model = Applyers
        fields = "__all__"
        