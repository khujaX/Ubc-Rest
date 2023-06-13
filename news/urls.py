from django.urls import path, include, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
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
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)