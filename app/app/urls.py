from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from main import views as main_views, urls as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='index'),
    path('api/v1/', include(main_urls)),  # Подключаем маршруты из main/urls.py
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)