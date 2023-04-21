from django.db import models
from user.models import User
from lead.models import Lead
# Create your models here.
class Campaign(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Lead)
    mail_subject = models.CharField(max_length=100, null=True, blank=True)
    mail_body = models.TextField()
    schedule = models.DateTimeField(null=True)
    class Meta:
        db_table = 'campaign'