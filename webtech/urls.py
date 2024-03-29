from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('portifolio', views.portifolio, name='portifolio'),
    path('contact', views.myForm, name='myForm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
