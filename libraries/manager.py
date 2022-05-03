

from django.db import models


class CustomManager(models.Manager):
    '''
    Custom class to filter queries by items that are no deleted
    '''

    def get_queryset(self):
        
        return super().get_queryset().filter(deleted=False)