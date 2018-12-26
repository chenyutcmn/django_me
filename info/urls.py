from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
        path('', views.freedom, name = 'freedom'),
        path('freedom', views.freedom, name = 'freedom'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

