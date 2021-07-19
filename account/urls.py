from rest_framework.routers import SimpleRouter
from account import views


router = SimpleRouter()

router.register(r'userprofile', views.UserProfileViewSet)

urlpatterns = router.urls
