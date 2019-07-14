
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),

    url('oauth', include('social_django.urls', namespace='social')),
    # url(r'^ravepay/', include(('ravepay.urls', 'ravepay'), namespace='ravepay')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
