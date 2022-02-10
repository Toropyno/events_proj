import datetime

from django.contrib.auth import get_user_model
from django.core.mail import send_mass_mail

from events.models import Event
from events_proj import settings

User = get_user_model()


def check_events(days=None):
    """
    Проверяет наличие событий на определенную дату относительно текущей.

    Если days не указан, то проверяются события на сегодняшний день.

    :param days: количество дней, прибавляемых к текущей дате

    :return: queryset событий на указанную дату
    """
    if days:
        estimated_date = datetime.datetime.now() + datetime.timedelta(days=days)
    else:
        estimated_date = datetime.datetime.now()
    return Event.objects.filter(date=estimated_date)


def report_about_events(events, days=None):
    """
    Оповещает пользователей о событиях текущих или приближающихся.

    Отправляем пользователям, причастным к событиям events, сообщение на почту
     с перечислением событий и их описанием.

    :param events: queryset событий
    :param days: количество дней, прибавляемых к текущей дате
    """
    # формируем данные для рассылки
    data = []
    if days:
        estimated_date = datetime.datetime.now() + datetime.timedelta(days=days)
        mail_subject = f'События на {estimated_date.date()}'  # Тема сообщения
    else:
        mail_subject = 'События на сегодня'  # Тема сообщения

    user_emails = events.values_list('creator__email', flat=True).distinct()
    for email in user_emails:
        mail_message = ''  # текст сообщения
        events_for_user = events.filter(creator__email=email)
        for e in events_for_user:
            mail_message += f'Событие "{e.title}", описание: {e.description}\n'
        data.append((mail_subject, mail_message, settings.EMAIL_HOST_USER, [email]))

    # отправляем данные
    send_mass_mail(datatuple=tuple(data))
