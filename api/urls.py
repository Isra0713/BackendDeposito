from django.urls import path, include
from rest_framework import routers
from api.views import ClienteViewSet, ProductoViewSet, PedidoViewSet, DetallePedidoViewSet


router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detallepedidos', DetallePedidoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]
