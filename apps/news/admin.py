from django.contrib import admin


from apps.news import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status']
    list_filter = ['status']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}