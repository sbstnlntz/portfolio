from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.views.i18n import set_language

# ============================================================
# Internationalized URL patterns
# Adds language prefixes (e.g., /en/, /de/)
# ============================================================
urlpatterns = i18n_patterns(
    path('', include('portfolio.urls')),  # Main portfolio app
    path('admin/', admin.site.urls),      # Django admin interface
)

# ============================================================
# Language switch endpoint for language toggle form
# ============================================================
urlpatterns += [
    path('i18n/setlang/', set_language, name='set_language'),
]

# ============================================================
# Serve media files locally during development
# ============================================================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
