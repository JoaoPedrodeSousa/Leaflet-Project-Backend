from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from imageRepository.views import UserViewSet, CategoryViewSet, LocationViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'categories',CategoryViewSet)
router.register(r'locations',LocationViewSet)
router.register(r'images',ImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
