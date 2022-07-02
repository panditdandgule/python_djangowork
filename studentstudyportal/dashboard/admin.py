from django.contrib import admin
from .models import *

# Register your models here.
admin.site.index_title='Student Study Portal'
admin.site.site_header='Admin Student Study Portal Dashboard'
admin.site.site_title='Student Study Portal'


class NotesAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
    list_display_links = ('id','title')
    list_editable = ('description',)

class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id','subject','title','description','due','is_finished')
    list_display_links = ('id', 'title')
    list_editable = ('is_finished',)

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_finished')
    list_display_links = ('id', 'title')
    list_editable = ('is_finished',)


admin.site.register(Notes,NotesAdmin)
admin.site.register(Homework,HomeworkAdmin)
admin.site.register(Todo,TodoAdmin)