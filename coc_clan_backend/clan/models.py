from django.db import models

class Member(models.Model):
    ROLE_CHOICES = [
        ('leader', 'Leader'),
        ('co', 'Co-Leader'),
        ('elder', 'Elder'),
        ('member', 'Member'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('warning', 'Warning'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    # tag = models.CharField(max_length=20, unique=True)
    tag = models.CharField(max_length=20, unique=True, null=True, blank=True)
    town_hall = models.IntegerField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    trophies = models.IntegerField(default=0)
    donations = models.IntegerField(default=0)
    donations_received = models.IntegerField(default=0)
    war_attacks_used = models.IntegerField(default=0)
    performance = models.FloatField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    last_active = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name