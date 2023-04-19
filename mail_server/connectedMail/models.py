from django.db import models
from user.models import User

# Create your models here.
class ConnectedMail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mail = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'connected_mail'