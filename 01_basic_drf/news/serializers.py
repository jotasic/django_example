from datetime import datetime
from django.db.models import fields
from rest_framework import exceptions
from django.utils.timesince import timesince
from rest_framework import serializers

from .models import Article, Journallist

   

class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Article
        exclude = ('id',)

    def get_time_since_publication(self, object):
        return timesince(object.publication_date, datetime.now())

    def validate(self, data):
        if data['title'] == data['description']:
            raise exceptions.ValidationError('Title and Description must be different in another')
        return data

    def validate_title(self, value):
        if len(value) < 30 :
            raise exceptions.ValidationError('The title has to be at least 30 chars long!')
        return value

class JournallistSerializer(serializers.ModelSerializer):
    article_set = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='article-detail')
    #article_set = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journallist
        fields = '__all__'