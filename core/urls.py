from django.urls import path
from rest_framework.routers import DefaultRouter

from core.views import TaskResultViewSet, get_riddle_answer


router = DefaultRouter()
router.register('task_results', TaskResultViewSet, basename='task_result')
urlpatterns = router.urls


urlpatterns += [
    path('get-riddle-answer/', get_riddle_answer, name='get_riddle_answer')
]
