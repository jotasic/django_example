from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers    import QuoteSerializer
from .models         import Quote
from api.pagination  import BigPagePagination
from api.permissions import IsAdminUserOrReadOnly, IsAuthorOrReadOnly

class QuoteListCreateAPIView(ListCreateAPIView):
    queryset           = Quote.objects.all().order_by('-id')
    serializer_class   = QuoteSerializer
    pagination         = BigPagePagination
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

class QuoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset           = Quote.objects.all()
    serializer_class   = QuoteSerializer
    permission_classes = [IsAuthorOrReadOnly]