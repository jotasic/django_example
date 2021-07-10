from django.db import models

from django.contrib.auth.models import User

class Quote(models.Model):
    author     = models.ForeignKey(User, on_delete=models.CASCADE)
    body       = models.TextField()
    context    = models.TextField()
    source     = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    class Meta:
        db_table = 'quotes'