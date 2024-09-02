from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/articles/', include("articles.urls")),
    path('api/v1/accounts/', include("accounts.urls")),
    path('api/v1/products/', include("products.urls")),
    path('api/v1/chatgpt/', include("chatgpt.urls")),
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]


urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
