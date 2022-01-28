from django.contrib import admin
from cars.models import Car
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail_preview','car_title','body_style','year','model','fuel_type','transmission','is_featured' ,'created_date')
    list_display_links = ('id','thumbnail_preview','car_title')
    list_editable = ('is_featured',)
    search_fields = ('id','car_title','model','body_style','year','fuel_type','city')
    list_filter = ('city','fuel_type','body_style','transmission')
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'photo'
    thumbnail_preview.allow_tags = True

admin.site.register(Car,CarAdmin)