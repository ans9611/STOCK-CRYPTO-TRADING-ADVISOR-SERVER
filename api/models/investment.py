from django.db import models
from django.contrib.auth import get_user_model

class Investment(models.Model):
  balance = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True)
  note = models.TextField(null=True, blank=True)
  risk = models.TextField(null=True, blank=True)
  account = models.ForeignKey(
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
