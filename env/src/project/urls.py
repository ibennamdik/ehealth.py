from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin 

urlpatterns = [
	url(r'^$', include("frontdesk.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include("usermanagement.urls")),
    url(r'^frontdesk/', include("frontdesk.urls")),
    url(r'^patient/', include("patient.urls")),
    url(r'^consultingroom/', include("consultingroom.urls")),
    url(r'^account/', include("account.urls")),
    url(r'^bloodbank/', include("bloodbank.urls")),
    url(r'^inventory/', include("inventory.urls")),
    url(r'^laboratory/', include("laboratory.urls")),
    url(r'^theatre/', include("theatre.urls")),
    url(r'^wards/', include("wards.urls")),
    url(r'^pharmacy/', include("pharmacy.urls")),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
