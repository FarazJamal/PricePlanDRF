from rest_framework import serializers
from .models import App, Plan, Subscription

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'user', 'name', 'description']


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'price']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'app', 'plan', 'active']
