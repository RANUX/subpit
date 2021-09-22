from django.contrib import admin
from .models import Subscriber

@admin.register(Subscriber)
class SubscriberModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'host')
