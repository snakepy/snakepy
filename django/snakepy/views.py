from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from rest_framework import viewsets
from snakepy import serializers
import rest_framework


s = [serializers.__dict__[i] for i in serializers.__dict__ if isinstance(
    serializers.__dict__[i], 
    rest_framework.serializers.SerializerMetaclass
)]

for i in s:

    locals()[
        i.Meta.model.__name__ + 'ViewSet',
    ] = type(
        i.Meta.model.__name__ + 'ViewSet', 
        (viewsets.ModelViewSet,), 
        {
            'queryset': i.Meta.model.objects.all(),
            'serializer_class': i,
            '__module__': __name__,    
        }
    )

