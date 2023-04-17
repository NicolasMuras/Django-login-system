from django.db import models
from simple_history.models import HistoricalRecords
from core.models import BaseModel
from users.models import User


class Resource(BaseModel):
    value = models.CharField(max_length=100, unique=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'

    def __str__(self):
        return self.value
