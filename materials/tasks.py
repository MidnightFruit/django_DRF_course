from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


logger = get_task_logger(__name__)

@shared_task
def send_notifications(course_name, subs):
    """
    Функция выполняющая рассылку об изменении курса.
    При выполнении в консоль выводится информация с названием курса и количеством удачно отправленных писем.
    :param course_name: Название курса.
    :param subs: Список состоящий из почт подписчиков.
    """
    send_status = send_mail(subject=f'Курс с названием: "{course_name}" был обновлён.', message=f'Здравствуйте, курс "{course_name}" был обновлён.\n',
              from_email=EMAIL_HOST_USER, recipient_list=subs)
    logger.info(f"Рассылка по {course_name}: {send_status}")


