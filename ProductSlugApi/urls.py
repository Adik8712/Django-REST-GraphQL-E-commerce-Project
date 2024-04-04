from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, permissions
from api_main.views import ProductViewSet, CategoryViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Product API",
        default_version='v1',
        description="API Documentation",
        contact=openapi.Contact(
            name="Adik",
            url="https://github.com/Adik8712",
            email="abashevadil12@gmail.com"
            ),
        license=openapi.License(
            name="BSD License",
            # url="",
            ),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns = [
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0),
                                                    name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), 
                                                    name="schema-redoc"),
    
    path('api/', include(router.urls)),
    path('graphql/', include('graphqlapi.urls')),
    path('admin/', admin.site.urls),
    path('redoc/', include('django.contrib.admindocs.urls')),
    path("", include("main.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)