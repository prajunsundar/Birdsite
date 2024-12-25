from django.contrib import admin
from .models import Birds
class BirdDetails(admin.ModelAdmin):
    list_display = ('name','domain','slug')
    prepopulated_fields = {'slug':('name','domain')}

admin.site.register(Birds,BirdDetails)
