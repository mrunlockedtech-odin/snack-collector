from django.db import models
from django.urls import reverse

# Create your models here.
class Snack(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=20)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("snacks_detail", kwargs={"snack_id": self.id})
  