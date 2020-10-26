from django.urls import path
from . import views
#For images:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('stage/<slug:slug>', views.stage, name='stage'),
    
]
