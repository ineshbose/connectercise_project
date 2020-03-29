from django.contrib import admin
from connectercise.models import Sport, SportRequest, UserProfile, Comment
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

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'request', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Sport, SportAdmin)
admin.site.register(SportRequest, RequestAdmin)
admin.site.register(UserProfile)