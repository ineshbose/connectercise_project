from django.contrib import admin
from main.models import UserProfile, SportingRequest

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','pageURL','email','sport', 'location', 'socialMedia')

class SportingRequestAdmin(admin.ModelAdmin):
    list_display = ('time', 'location', 'sessionID', 'sport')

#admin.site.register(UserProfile, UserAdmin)
#admin.site.register(SportingRequest, SportingRequestAdmin)
admin.site.register(UserProfile)
admin.site.register(SportingRequest)