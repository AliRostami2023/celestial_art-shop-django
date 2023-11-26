from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('home_module.urls')),
    path('', include('account_module.urls')),
    path('products/', include('product_module.urls')),
    path('cart/', include('order_module.urls')),
    path('dashboard/', include('dashboard_user.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

