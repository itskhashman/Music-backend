import graphene
from app.schema import Query, Mutation

schema = graphene.Schema(query=Query , mutation=Mutation)
