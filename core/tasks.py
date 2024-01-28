import json
import random

from consumer import celery_app


@celery_app.task
def answer_riddle(riddle_data):
    wise_choice = random.choice(riddle_data['choices'])
    result = {"chosen_answer": wise_choice, "webhook_url": riddle_data["webhook_url"]}
    return result
