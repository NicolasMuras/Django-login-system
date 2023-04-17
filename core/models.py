from django.db import models


class BaseModel(models.Model):
    """
        Abstract class to use with simple history, this help us to track the state of the file.
    """
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('State', default=True)
    created_date = models.DateField('Creation Date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Update Date', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Deletion Date', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Models'
