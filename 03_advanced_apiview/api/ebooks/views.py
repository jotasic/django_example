from rest_framework          import generics, pagination
from rest_framework.generics import get_object_or_404
 
from api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from api.pagination import SmallSetPagination
from .serializers    import EbookSerializer, ReviewSerializer
from .models         import Ebook, Review

class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by('-id')
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        review_author = self.request.user
        serializer.save(ebook=ebook, review_author=review_author) 

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# same
# class EbookListCreateAPIView(mixins.ListModelMixin,
    #                          mixins.generics.CreateAPIView,
    #                         generics.GenericAPIView):

    # queryset = Ebook.objects.all()
    # serializers_class = EbookSerializer

    # def get(self, req uest, *args, **kwargs):
    #     return self.list(request, *args, ** kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, ** kwargs):
