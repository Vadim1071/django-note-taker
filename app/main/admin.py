# Register your models here.
from django.contrib import admin
from .models import Application, Note, Tag

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at', 'modified_at')
    list_filter = ('tags','created_at', 'modified_at')
    search_fields = ('user__username', 'title', 'content')

admin.site.register(Tag)
admin.site.register(Application)

