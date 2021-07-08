from django.db import models
from django.db.models.base import Model

class JobOffer(models.Model):
    company_name    = models.CharField(max_length=50)
    company_email   = models.EmailField()
    job_title       = models.CharField(max_length=100)
    job_description = models.TextField()
    salary          = models.IntegerField()
    city            = models.CharField(max_length=50)
    state           = models.CharField(max_length=50)
    created_at      = models.DateTimeField(auto_now_add=True)
    available       = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.company_name} - {self.job_title}'

    class Meta:
        db_table = 'job_offers'

