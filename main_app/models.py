from django.db import models
from django.urls import reverse

# Create your models here.
TYPES = (
  ('Chips','Chips'),
  ('Cookies','Cookies'),
  ('Fruit','Fruit'),
  ('Veggies','Veggies')
)
class Snack(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=20, choices = TYPES, default=TYPES[0])
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("snacks_detail", kwargs={"snack_id": self.id})

class Purchase(models.Model):
  purchase_date = models.DateField('Purchase Date')
  store_name = models.CharField(max_length=50)
  snack = models.ForeignKey(Snack, on_delete=models.CASCADE)

  def __str__(self):
    return f"This item was purchased at {self.store_name} on {self.purchase_date}"