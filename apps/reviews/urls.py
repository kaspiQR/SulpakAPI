from rest_framework.routers import DefaultRouter
from .views import CommentModelViewSet, StarsModelViewSet


router = DefaultRouter()

router.register('comment', CommentModelViewSet)
router.register('stars', StarsModelViewSet)

urlpatterns = router.urls