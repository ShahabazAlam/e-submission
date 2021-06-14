from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
import application

admin.site.site_header = "E-SUBMI$$ION Admin"
admin.site.site_title = "E-SUBMI$$ION Admin Portal"
admin.site.index_title = "WELCOME TO E-SUBMI$$ION"
urlpatterns = [
    path('', include('application.urls', namespace='application')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
