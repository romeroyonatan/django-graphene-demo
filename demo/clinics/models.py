from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=30)
    number = models.PositiveIntegerField()

    def __str__(self):
        return '{} {}'.format(self.street, self.number)


class Clinic(models.Model):
    name = models.CharField(max_length=30)
    address = models.ForeignKey(Address)
    doctor = models.ForeignKey('doctors.Doctor', related_name='clinics')

    def __str__(self):
        return self.name
