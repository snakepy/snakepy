import graphene
import json
from graphene_django.types import DjangoObjectType

import snakepy.models as models
import snakepy.serializers as serializers

m = dict([(name, cls) for name, cls in models.__dict__.items() if isinstance(cls, type)])
s = dict([(name, cls) for name, cls in serializers.__dict__.items() if isinstance(cls, type)])

def field_func(i, n):
    def _function(self, info):
        return s[i+'Serializer'](self).data
    return _function

for i in m:

    locals()[
        i + 'Type'
    ] = type(
        i + 'Type', 
        (DjangoObjectType,), 
        dict([
            ['__module__', __name__,],
            [
                'Meta',
                type('Meta', tuple(), {
                    'model': m[i],
                })
            ],
        ])
    )

def make_func(n):
    def _function(self, info, **kwargs):
        return n.objects.all()
    return _function

l = locals()
locals()[
        'Query'
    ] = type(
        'Query', 
        (graphene.ObjectType,),
        dict([(
                'all_'+i.lower()+'s', graphene.List(l[i + 'Type']),
        ) for i in m] + [(
                'resolve_all_'+i.lower()+'s', make_func(m[i]),
        ) for i in m])
    )


schema = graphene.Schema(query=Query, auto_camelcase=False)

