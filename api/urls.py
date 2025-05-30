from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r"blog", views.BlogView, basename="blog")

urlpatterns = router.urls