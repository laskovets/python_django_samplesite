from django.contrib import admin

# Register your models here.
from django.apps import apps
from bboard.models import Bb, Rubric

app = apps.get_app_config('bboard')


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


# for model_name, model in app.models.items():
#     admin.site.register(model)

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
