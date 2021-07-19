from rest_framework.routers import SimpleRouter
from exercise import views


router = SimpleRouter()

router.register(r'heartsong', views.HeartSongViewSet)
router.register(r'program', views.ProgramViewSet)
router.register(r'duration', views.DurationViewSet)
router.register(r'plan', views.PlanViewSet)
router.register(r'goal', views.GoalViewSet)

urlpatterns = router.urls
