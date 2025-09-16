# movies/admin.py
from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
    list_display = ('name', 'price', 'amount_left')  # helpful

    def get_readonly_fields(self, request, obj=None):
        base = super().get_readonly_fields(request, obj)
        if obj and obj.amount_left == 0:
            return (*base, 'amount_left')
        return base

admin.site.register(Movie, MovieAdmin)