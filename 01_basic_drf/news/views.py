from django.db.models import manager
from django.utils.translation import activate
from news.models import Article, Journallist
from django.utils.cache import patch_response_headers
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .serializers import ArticleSerializer, JournallistSerializer

class ArticleListCreateAPIView(APIView):
    def get(self, request):
        articles   = Article.objects.filter(activate=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ArticleDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        article    = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article    = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class journallistListCreateAPIView(APIView):
    def get(self, request):
        journallist = Journallist.objects.all()
        serializer  = JournallistSerializer(instance=journallist, 
                                            many=True,
                                            context={'request' : request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = JournallistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class journallistDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Journallist, pk=pk)

    def get(self, request, pk):
        journallist = self.get_object(pk)
        serializer = JournallistSerializer(instance=journallist, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        journallist = self.get_object(pk)
        serializer = JournallistSerializer(instance=journallist, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        journallist = self.get_object(pk)
        serializer = JournallistSerializer(instance=journallist, many=False)
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        