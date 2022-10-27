from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["link"]
