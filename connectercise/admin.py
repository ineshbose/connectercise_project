from django.contrib import admin
from connectercise.models import Sport, SportRequest

# Register your models here.

class SportAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class RequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'sport', 'url']

admin.site.register(Sport, SportAdmin)
admin.site.register(SportRequest, RequestAdmin)