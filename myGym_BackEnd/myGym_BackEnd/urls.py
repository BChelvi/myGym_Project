from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myGym_data.views import UserViewSet, CustomTokenObtainPairView, WorkoutProgramViewSet, WeekProgramViewSet, SeriesViewSet, DayProgramViewSet, ExerciceViewSet, PerformanceViewSet, ProgressUserViewSet
# from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'programs', WorkoutProgramViewSet)
router.register(r'weeks', WeekProgramViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'days', DayProgramViewSet)
router.register(r'exercices', ExerciceViewSet)
router.register(r'progress', ProgressUserViewSet)
router.register(r'performances', PerformanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
