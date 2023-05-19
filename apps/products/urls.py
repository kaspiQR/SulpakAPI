from rest_framework.routers import DefaultRouter
from .views import ProductModelViewSet, CategoryModelViewSet


router = DefaultRouter()

router.register('category', CategoryModelViewSet)
router.register('products', ProductModelViewSet)

urlpatterns = router.urls