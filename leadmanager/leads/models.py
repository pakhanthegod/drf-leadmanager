from django.db import models
from django.contrib.auth import get_user_model


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(get_user_model(), related_name='leads', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)