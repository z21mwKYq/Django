from django.contrib import admin
from .models import Bb
from .models import Rubric


# Register your models here.
class BbAdmin (admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)

class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric, RubricAdmin)
