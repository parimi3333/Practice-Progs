from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import profile
from django.contrib.auth.models import User