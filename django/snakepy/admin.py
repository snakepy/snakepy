from django.contrib import admin

# Register your models here.

import snakepy.models as models


m = dict([(name, cls) for name, cls in models.__dict__.items() if isinstance(cls, type)])

for i in m:
    admin.site.register(m[i])

