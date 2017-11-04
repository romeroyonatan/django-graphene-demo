import graphene

from graphene_django import types

from . import models


class DoctorType(types.DjangoObjectType):
    class Meta:
        model = models.Doctor


class Query(graphene.ObjectType):
    doctors = graphene.List(DoctorType)
    doctor = graphene.Field(DoctorType,
                            id=graphene.Int(),
                            name=graphene.String())

    def resolve_doctors(self, info, **kwargs):
        return models.Doctor.objects.all()

    def resolve_doctor(self, info, id=None, **kwargs):
        if id is not None:
            return models.Doctor.objects.get(pk=id)
