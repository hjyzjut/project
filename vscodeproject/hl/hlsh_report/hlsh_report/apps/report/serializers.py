from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import *

class GmvBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = GmvBudget
        fields = '__all__'


class GmvGsvRealSerializer(serializers.ModelSerializer):
    class Meta:
        model = GmvGsvReal
        fields = '__all__'


class GmvWeekRealSerializer(serializers.ModelSerializer):
    class Meta:
        model = GmvWeekReal
        fields = '__all__'

class GuaranteedLicenseIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuaranteedLicenseIncome
        fields = '__all__'


class RealLicenseIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealLicenseIncome
        fields = '__all__'

class AuthorizedShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizedShop
        fields = '__all__'


class DoubleElevenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoubleEleven
        fields = '__all__'