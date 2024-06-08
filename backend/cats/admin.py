from cats.models import Cat
from django.contrib import admin


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass
