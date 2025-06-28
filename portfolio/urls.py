from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# ============================================================
# Main URL configuration for the portfolio app
# ============================================================
urlpatterns = [
    path('', views.home, name='home'),  # Landing page view
]

# ============================================================
# Serve media files locally during development (DEBUG mode)
# ============================================================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
