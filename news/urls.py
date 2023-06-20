from django.urls import path, include, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('News', NewsViewset)
router.register('Categories', CategoryViewset)
router.register('Users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/users/', UserList.as_view()),
    path('api/v1/users/<int:pk>', UserDetail.as_view()),
    path('api/v1/users/create', UserCreate.as_view()),
    path('api/v1/users/details/<int:pk>', UserDetails.as_view()),
    path('api/v1/users/delete/<int:pk>', UserDelete.as_view()),
    path('api/v1/categories/', CategoryList.as_view()),
    path('api/v1/categories/create', CategoryCreate.as_view()),
    path('api/v1/categories/details/<int:pk>', CategoryDetail.as_view()),
    path('api/v1/news/', NewsList.as_view()),
    path('api/v1/news/create', NewsCreate.as_view()),
    path('api/v1/news/details/<int:pk>', NewsDetail.as_view()),
    path('api/v1/news/update/<int:pk>', NewsUpdate.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)