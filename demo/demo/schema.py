import graphene

import clinics.schema
import doctors.schema


class Query(clinics.schema.Query,
            doctors.schema.Query,
            graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
