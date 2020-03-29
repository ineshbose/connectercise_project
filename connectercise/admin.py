from django.contrib import admin
from connectercise.models import Sport, SportRequest, UserProfile, Comment

# Register your models here.

class SportAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class RequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'sport', 'desc']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('creator', 'body', 'request', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('creator', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Sport, SportAdmin)
admin.site.register(SportRequest, RequestAdmin)
admin.site.register(UserProfile)