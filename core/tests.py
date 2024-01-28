from django.test import TestCase, override_settings
from django_celery_results.models import TaskResult
from rest_framework_api_key.models import APIKey

from .tasks import answer_riddle


class YourAppTests(TestCase):

    def setUp(self):
        _, key = APIKey.objects.create_key(name="test")
        self.client.defaults['HTTP_AUTHORIZATION'] = f"Api-Key {key}"

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_answer_riddle_task(self):
        riddle_data = {'choices': ['option1', 'option2', 'option3'], 'webhook_url': 'https://example.com/webhook'}

        result = answer_riddle.delay(riddle_data)

        self.assertTrue(result.successful())

        self.assertEqual(result.result['webhook_url'], riddle_data['webhook_url'])
        self.assertIn(result.result['chosen_answer'], riddle_data['choices'])

    def test_task_result_viewset(self):
        task_result = TaskResult.objects.create(
            task_id='some_task_id', result='{"chosen_answer": "b", "webhook_url": "https://example.com/webhook"}'
        )

        response = self.client.get(f'/core/task_results/{task_result.task_id}/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data['task_id'], task_result.task_id)
        self.assertEqual(response.data['result'], task_result.result)
