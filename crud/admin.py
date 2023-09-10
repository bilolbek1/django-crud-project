from django.contrib import admin

from crud.models import People


# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    class Meta:
        model = People
        fields = ['id', 'name', 'surname', 'job']


admin.site.register(People, PeopleAdmin)
