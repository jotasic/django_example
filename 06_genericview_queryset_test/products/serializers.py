from rest_framework.serializers import ModelSerializer

from .models import Product


class ProdcutSerializer(ModelSerializer):
    class Meta:
        model  = Product
        fields = "__all__"