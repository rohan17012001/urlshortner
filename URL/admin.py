from django.contrib import admin
from .models import LongtoShort
# Register your models here.

admin.site.register(LongtoShort)
#after adding new models: run commands for makemigrations and migrate