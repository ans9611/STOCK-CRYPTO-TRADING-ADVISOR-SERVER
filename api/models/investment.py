from django.db import models
from django.contrib.auth import get_user_model

class Investment(models.Model):
  balance = models.DecimalField(max_digits=3, decimal_places=2)
  description = models.CharField(max_length=100)
  risk = models.BooleanField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"'{self.balance}' dollars invested"

  def as_dict(self):
    """Returns dictionary version of Investment models"""
    return {
        'id': self.id,
        'balance': self.balance,
        'risk': self.risk,
        'description': self.description
    }
