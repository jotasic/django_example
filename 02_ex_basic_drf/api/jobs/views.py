from rest_framework import response, views, status, generics

from .serializers   import JobOfferSerializer
from .models        import JobOffer

class JobOfferCreateListAPIView(views.APIView):
    def get(self, request):
        job_offers = JobOffer.objects.all()
        serializer = JobOfferSerializer(instance=job_offers, many=True)

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
            
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class JobOfferDetailAPIView(views.APIView):

    def get_object(self, pk):
        return generics.get_object_or_404(JobOffer, pk=pk)

    def get(self, request, pk):
        job_offer  = self.get_object(pk)
        serializer = JobOfferSerializer(instance=job_offer, many=False)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = JobOfferSerializer(data=request.data, many=False)
        
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        job_offer = self.get_object(pk)
        job_offer.delete()

        return response.Response(status=status.HTTP_204_NO_CONTENT)