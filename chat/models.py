from django.db import models
from utils.models import BaseModel


# Create your models here.
class Message(BaseModel):
    title = models.CharField(max_length=255)
