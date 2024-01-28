import requests
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_results.models import TaskResult


@receiver(post_save, sender=TaskResult)
def send_result_to_producer(sender, instance, **kwargs):
    print('Reached Signal Handler')
    headers = {'authorization': f'Api-Key {settings.RIDDLE_API_KEY}'}
    requests.post(
        f'{settings.PRODUCER_BASE_URL}', data={'chosen_answer': instance.result}, headers=headers
    )
