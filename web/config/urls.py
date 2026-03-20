from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# 🧬 SYSTEM URLS (ALWAYS ACCESSIBLE)
urlpatterns = [
    # 🌀 Health Check (Infrastructure)
    path('', include('apps.core.urls', namespace='core')),
    
    # ⚙️ Django Admin
    path('admin/', admin.site.urls),
]

# 🌍 LOCALIZED URLS (BILINGUAL)
urlpatterns += i18n_patterns(
    path('', include('apps.pages.urls', namespace='pages')),
    prefix_default_language=False,  # RU remains default
)

# 🛠️ DEBUG TOOLBAR & STATIC UTILITY
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
