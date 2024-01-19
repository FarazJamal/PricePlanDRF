from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    name = models.CharField(max_length=100)
    PLAN_CHOICES = [
        ('Free', 'Free ($0)'),
        ('Standard', 'Standard ($10)'),
        ('Pro', 'Pro ($25)'),
    ]

    price = models.CharField(max_length=20, choices=PLAN_CHOICES, default='Free', unique=True)


    def __str__(self):
        return self.name

class App(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    app = models.OneToOneField(App, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.app.name} - {self.plan.name}"
