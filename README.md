# Consumer Project README

## Project Overview

This Django project serves as the consumer in a producer-consumer architecture. It interacts with a producer project to receive and process messages using Django REST Framework and Celery.

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd consumer_project

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

`pip install -r requirements.txt`

Create a .env file using the .env.example template

`python manage.py migrate`

Running the Server

`python manage.py runserver`

Running Celery Worker

`celery -A consumer_project worker -l info`

Run the tests

`python manage.py test`
