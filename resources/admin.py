from django.contrib import admin
from resources.models import Resource


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'owner')


admin.site.register(Resource, ResourceAdmin)