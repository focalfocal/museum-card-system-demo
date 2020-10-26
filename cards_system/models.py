from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.
class Child(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='the child name')
    #image = models.ImageField(default='', blank=True, upload_to='images')
    
    #The cloudinary.models.CloudinaryField defines a field in the model that represents an image stored in Cloudinary. Allows you to store references to Cloudinary stored images in your model. The internal type of the field is CharField.
    #Returns an CloudinaryResource object.
    #image = CloudinaryField('image', blank=True,null=True)
    image = CloudinaryField(   #photo for card
        "Image",
        overwrite = True,
        resource_type ="image",
        folder = 'museum_cards',
        use_filename = True,
        blank=True
        )
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, verbose_name = 'date the card is put in use')
    #slug = models.SlugField(max_length=250, unique_for_date='publish') 
    slug = models.SlugField(blank=True, default='')
    current_stage = models.IntegerField(default = 0, verbose_name = "Stage to be used as current when the card is inserted")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        #debugging:
        #print("url= ", self.image.url)
        #print("path= ", self.image.path)
        super(Child, self).save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    #'View on site' for the admin. Generates slug path
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])

class Stage_content(models.Model):
    child = models.ForeignKey('cards_system.Child', on_delete=models.CASCADE, related_name='stage_content')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    stage_number = models.IntegerField(verbose_name = "the stage number")
    text = models.TextField(verbose_name='the stage Englishtext')
    text_es = models.TextField(verbose_name='the stage Spanish text')
    image = CloudinaryField(   #photo for this stage content
        "Image",
        overwrite = True,
        resource_type ="image",
        folder = 'museum_cards/stage_content',
        use_filename = True,
        blank=True
        )
    image_text = models.TextField(verbose_name='the image accompanying English text')
    image_text_es = models.TextField(verbose_name='the image accompanying Spanish text')

    def __str__(self):
        return str(self.child) + " - stage #" + str(self.stage_number)
