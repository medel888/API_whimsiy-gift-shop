from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Creamos un enrutador y registramos el ProductViewSet
router = DefaultRouter()
router.register(r'', ProductViewSet)

# Definimos las URLs de la aplicación
urlpatterns = [
    path('', include(router.urls)),
]
