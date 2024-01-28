import json

import requests
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_results.models import TaskResult


@receiver(post_save, sender=TaskResult)
def send_result_to_producer(sender, instance, created, **kwargs):
    if not created:
        return

    headers = {'authorization': f'Api-Key {settings.RIDDLE_API_KEY}'}
    task_result = json.loads(instance.result)
    requests.post(
        task_result['webhook_url'],
        data={"chosen_answer": task_result['chosen_answer']},
        headers=headers
    )
