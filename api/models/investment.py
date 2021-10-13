from django.db import models
from django.contrib.auth import get_user_model

class Investment(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  balance = models.DecimalField(decimal_places=2)
  note = models.CharField(max_length=100)
  risk = models.BooleanField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The investment amount is '{self.balance}' dollars. It is {self.risk} risk."

  def as_dict(self):
    """Returns dictionary version of Investment models"""
    return {
        'id': self.id,
        'balance': self.balance,
        'risk': self.risk,
        'note': self.note
    }
