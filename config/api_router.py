from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from backend.companies.api.views import CompanyViewSet
from backend.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("companies", CompanyViewSet)

app_name = "api"
urlpatterns = router.urls
