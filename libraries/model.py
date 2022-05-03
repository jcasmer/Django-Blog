import datetime

from django.db import models
from django.contrib.auth.models import User

from libraries.manager import CustomManager


class BaseModel(models.Model):
    '''
    Base model
    '''
    deleted = models.BooleanField('Deleted', default=False)

    objects = CustomManager()

    def delete(self):
        '''
        Soft delete
        '''
        self.deleted = True
        self.save()

  
    class Meta:
        abstract = True