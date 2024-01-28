from django_celery_results.models import TaskResult
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from core.serializers import TaskResultSerializer
from core.tasks import answer_riddle


@api_view(['POST'])
@permission_classes([HasAPIKey])
def get_riddle_answer(request):
    task = answer_riddle.delay(request.data)
    return Response({"task_id": task.id})


class TaskResultViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing celery task results.
    """

    permission_classes = [HasAPIKey | IsAuthenticated]
    lookup_field = 'task_id'
    queryset = TaskResult.objects.all()
    serializer_class = TaskResultSerializer
