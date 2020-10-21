from django.contrib import admin

# Register your models here.
from .models import Child, Stage_content

admin.site.register(Child)
admin.site.register(Stage_content)