
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from car_collection_app.web.views import ProfileViewSet, CarViewSet

router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('cars', CarViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car_collection_app.web.urls')),
    path('', include(router.urls)),
]
