from rest_framework.routers import DefaultRouter
from .views import VerificationEmailModelViewSet, ConfirmCodeModelViewSet

router = DefaultRouter()

router.register('send_code', VerificationEmailModelViewSet)
router.register('confirm_code', ConfirmCodeModelViewSet)

urlpatterns = router.urls
