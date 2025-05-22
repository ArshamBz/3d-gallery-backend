from django.contrib import admin
from .models import Room, Image


class ImageAdmin(admin.TabularInline):
    model = Image
    extra = 1
    show_change_link = True


class RoomAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageAdmin]


admin.site.register(Room, RoomAdmin)
# admin.site.register(Image)
