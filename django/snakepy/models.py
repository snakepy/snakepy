from django.db import models
import json

# Create your models here.

m = json.loads(open('./models.json').read())

for i in m['models']:

    locals()[i] = type(i, (models.Model,), 
        dict([
            [j, models.TextField(default='', blank=True, null=True, )] for j in m['models'][i]
        ]+[
            ['__module__', __name__,]
        ])
    )

