from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'hobbyapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
