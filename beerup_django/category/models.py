from django.db import models


# Create your models here.
class Category (models.Model):
    '''
    Category model
    '''
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural= ('categories')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'