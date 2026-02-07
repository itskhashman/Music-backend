from django.contrib import admin # admin site -- Needed so /admin/ works
from django.urls import path # path() is how Django maps URL → view ---- Every URL in Django is registered using path
from graphene_django.views import GraphQLView # The engine that runs GraphQL requests
from django.views.decorators.csrf import csrf_exempt # disable CSRF Attack.

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
