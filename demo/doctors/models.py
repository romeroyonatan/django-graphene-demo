from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return '{}, {}'.format(self.last_name.upper(), self.first_name)
