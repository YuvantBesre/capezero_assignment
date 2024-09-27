from django.contrib import admin
from .models import Deal, Project

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fmv',)
    list_display_links = ('id', 'name',)
    readonly_fields = ('created', 'created',)


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tax_credit_transfer_rate',)
    list_display_links = ('id', 'name',)
    readonly_fields = ('created', 'created',)
    filter_horizontal = ('projects',)