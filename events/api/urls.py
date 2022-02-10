from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.CreateUserViewSet)
router.register(r'events', views.EventViewSet, basename='event')

urlpatterns = router.urls
