#for image handling
from io import BytesIO
from PIL import Image

#django
from django.core.files import File
from django.db import models
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

#other apps from project
from category.models import Category


'''Product models'''

class Product(models.Model):
    '''
    Product model
    '''
    category = ForeignKey(Category, related_name='product',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000'+ self.image.url
        else:
            return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000'+ self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
            
                return 'http://127.0.0.1:8000'+ self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self,image,size=(300,200)):
        '''create thumbnail '''

        img = Image.open(image)
        thumb_io = BytesIO()
        print('modo imagen'+ img.mode)


        if img.mode in ["RGBA", "P"]:
            img = img.convert("RGB")
            img.thumbnail(size)
            img.save(thumb_io, format='JPEG', quality=85)
            thumbnail = File(thumb_io, name=image.name)
        else:
            
            img.thumbnail(size)
            img.save(thumb_io, format='JPEG', quality=85)
            thumbnail = File(thumb_io, name=image.name)
        

        return thumbnail

