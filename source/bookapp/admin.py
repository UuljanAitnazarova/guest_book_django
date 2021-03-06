from django.contrib import admin

from bookapp.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'text', 'status']
    list_filter = ['status']
    search_fields = ['author']
    fields = ['author', 'email', 'text', 'status', 'created_at', 'updated_at']


admin.site.register(GuestBook, GuestBookAdmin)