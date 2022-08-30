from django.db import models


class Transaction(models.Model):
    bcs_id = models.IntegerField(null=False)
    description = models.TextField(max_length=500, null=True, blank=True)
