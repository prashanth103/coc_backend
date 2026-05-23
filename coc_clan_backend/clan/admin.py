from django.contrib import admin
from .models import Member, War, Attack

# Register your models here.
admin.site.register(Member)
admin.site.register(War)
admin.site.register(Attack)