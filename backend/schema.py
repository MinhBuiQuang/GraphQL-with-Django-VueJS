import graphene

import home.schema


class Query(home.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutations(home.schema.SinhVienMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutations)
