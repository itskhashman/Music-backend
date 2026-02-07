import graphene
from backend.schema import Query, Mutation

schema = graphene.Schema(query=Query , mutation=Mutation)
