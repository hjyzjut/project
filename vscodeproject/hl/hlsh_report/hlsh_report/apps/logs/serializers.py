from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import OperateLog

class OperateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperateLog
        fields = '__all__'