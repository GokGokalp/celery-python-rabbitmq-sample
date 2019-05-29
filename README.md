Prerequisites:
---
pip3 install celery
pip3 install flower

First start celery worker:
---
celery -A celery_example worker --loglevel=info

Then run tasks:
---
python3 -m celery_example.run_tasks

Dashboard with flower:
---
celery -A celery_example flower