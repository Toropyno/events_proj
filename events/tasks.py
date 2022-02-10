from celery import shared_task
from . import services


# проверка событий на сегодня
@shared_task
def check_events_for_today_task():
    events = services.check_events()
    services.report_about_events(events)


# проверка событий на завтра
@shared_task
def check_events_for_tomorrow_task():
    events = services.check_events(1)
    services.report_about_events(events, 1)


# проверка событий
@shared_task(bind=True)
def check_events(self, days=None):
    events = services.check_events(days)
    services.report_about_events(events, days)
