from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Quote

class QuoteSerializer(ModelSerializer):
    author = StringRelatedField(read_only=True)

    class Meta:
        model = Quote
        fields = '__all__'