import graphene

from graphene_django import types

from . import models


class AddressType(types.DjangoObjectType):
    class Meta:
        model = models.Address


class ClinicType(types.DjangoObjectType):
    class Meta:
        model = models.Clinic


class Query(graphene.ObjectType):
    clinics = graphene.List(ClinicType)

    def resolve_clinics(self, info, **kwargs):
        return models.Clinic.objects.all()
