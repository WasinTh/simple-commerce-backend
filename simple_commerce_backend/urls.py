from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/shop/', include('shop.urls')),
    path('api/catalog/', include('catalog.urls')),
    path('api/sale/', include('sale.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
