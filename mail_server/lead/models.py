from django.db import models

# Create your models here.
class Lead(models.Model):
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    company_desc = models.CharField(max_length=150, blank=True, null=True)
    company_site = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lead'