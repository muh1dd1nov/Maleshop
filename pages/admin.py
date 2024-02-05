from django.contrib import admin
from pages.models import *

@admin.register(MainCarusel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['titlesmall', 'titlebig','created_at','updated_at']
    search_fields = ['title','info']
    list_filter = ('is_active',)
