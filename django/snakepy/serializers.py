from rest_framework import serializers

import snakepy.models as models

from django.db.models.query_utils import DeferredAttribute

m = dict([(name, cls) for name, cls in models.__dict__.items() if isinstance(cls, type)])

for i in m:

    locals()[
        m[i].__name__+'Serializer'
    ] = type(
        m[i].__name__+'Serializer', 
        (serializers.HyperlinkedModelSerializer,), 
        dict([
            ['__module__', __name__,],
            [
                'Meta',
                type('Meta', tuple(), {
                    'model': m[i],
                    'fields': tuple(
                        [j for j in m[i].__dict__ if isinstance(
                            m[i].__dict__[j], 
                            DeferredAttribute
                        )] # + ['url']
                    ),
                })
            ]
        ])
    )
