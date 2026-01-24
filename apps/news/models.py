from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class News(models.Model):

    class Status_choices(models.TextChoices):
        Draft = 'DF','Draft'
        Published = 'PB','Published'
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/')
    publish_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status_choices.choices, default=Status_choices.Draft)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_time']
        verbose_name = 'New'
        verbose_name_plural = 'News'
