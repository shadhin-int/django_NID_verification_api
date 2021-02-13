from django.db import models


class NIDInfo(models.Model):
    nid_number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
