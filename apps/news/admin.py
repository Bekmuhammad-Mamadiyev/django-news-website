from django.contrib import admin


from apps.news import models
from apps.news.models import Contact


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'slug', 'publish_time', 'status']
    list_filter = ['status']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Contact)