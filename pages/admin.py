from django.contrib import admin
from pages.models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','thumbnail_preview','first_name','created_date')
    list_display_links = ('id','first_name','thumbnail_preview')
    search_fields = ('first_name','last_name','designation')
    list_filter = ('designation',)
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'photo'
    thumbnail_preview.allow_tags = True

admin.site.register(Team, TeamAdmin)