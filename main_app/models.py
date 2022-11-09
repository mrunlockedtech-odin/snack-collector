from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta

# Create your models here.
class Dish(models.Model):
  url = models.CharField(max_length = 2048)
  dish_name = models.CharField(max_length = 50)

  def __str__(self):
    return self.dish_name
  
  def get_absolute_url(self):
      return reverse("dishes_detail", kwargs={"pk": self.id})
  


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
  dishes = models.ManyToManyField(Dish)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("snacks_detail", kwargs={"snack_id": self.id})
  
  def purchased_in_month(self):
    output = False
    for num in range(0,31):
      if(self.purchase_set.filter(purchase_date=datetime.today()-timedelta(days=num)).count() > 0):
        output = True
    return output


class Purchase(models.Model):
  purchase_date = models.DateField('Purchase Date')
  store_name = models.CharField(max_length=50)
  snack = models.ForeignKey(Snack, on_delete=models.CASCADE)

  def __str__(self):
    return f"This item was purchased at {self.store_name} on {self.purchase_date}"

  class Meta:
    ordering = ['-purchase_date']