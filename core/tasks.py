import random

from consumer import celery_app


@celery_app.task
def answer_riddle(riddle_data):
    wise_choice = random.choice(riddle_data['choices'])
    return wise_choice
