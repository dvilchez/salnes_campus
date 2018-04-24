from django.contrib import admin
from .models import Lead

# Register your models here.
class LeadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lead, LeadAdmin)