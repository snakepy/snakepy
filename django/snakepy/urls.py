from django.urls import include, path
from rest_framework import routers
from snakepy import views
from rest_framework import viewsets

v = [views.__dict__[k] for k in views.__dict__ if isinstance(
    views.__dict__[k], 
    type
) and issubclass(
    views.__dict__[k], 
    viewsets.ModelViewSet
)]


router = routers.DefaultRouter()

for i in v:
    router.register(
        i.serializer_class.Meta.model._meta.verbose_name_plural.title().lower(), 
        i,
    )

urlpatterns = [
    path('', include(router.urls)),
]