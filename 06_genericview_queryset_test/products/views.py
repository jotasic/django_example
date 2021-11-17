import datetime

from rest_framework.generics import ListCreateAPIView

from .models      import Product
from .serializers import ProdcutSerializer

class ProdcutListView(ListCreateAPIView):
    # queryset = Product.objects.filter(created_at__range = [datetime.datetime.now() - datetime.timedelta(seconds=30) , datetime.datetime.now()])
    serializer_class = ProdcutSerializer

    def get_queryset(self):
        return Product.objects.filter(created_at__range = [datetime.datetime.now() - datetime.timedelta(seconds=30) , datetime.datetime.now()])