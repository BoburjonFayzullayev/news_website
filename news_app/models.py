from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse
from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)

class Category(models.Model):
    name = models.CharField(max_length= 150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class News(models.Model):

    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)
    # slug = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft
                              )
    objects = models.Manager()  # default manager
    published = PublishedManager()

    class Meta:
        ordering = ["-publish_time"]
        verbose_name_plural = "News"
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail_page', args=[self.slug])

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    messege =models.TextField()

    def __str__(self):
        return self.email
