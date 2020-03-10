from django.contrib import admin
from connectercise.models import Sport, SportRequest, UserProfile
from django.forms.widgets import TextInput

from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField
# Register your models here.

class SportAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class RequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'sport', 'desc','address', 'geolocation' ]
    formfield_overrides = {
        AddressField: {
            'widget': GoogleMapsAddressWidget
        },
        GeoLocationField: {
            'widget': TextInput(attrs={
                'readonly': 'readonly'
            })
        },
    }
admin.site.register(Sport, SportAdmin)
admin.site.register(SportRequest, RequestAdmin)
admin.site.register(UserProfile)