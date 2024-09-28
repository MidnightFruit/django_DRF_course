from celery import shared_task
from django.contrib.auth import get_user_model
from celery.utils.log import get_task_logger

from users.models import User
from django.utils import timezone

logger = get_task_logger(__name__)


User = get_user_model()

@shared_task
def block_inactive_user():
    users = User.objects.all()
    today = timezone.now()

    for user in users:
        if (user.last_login - today).days > 30:
            user.update(is_active=False)
            logger.info(f"Пользователь {user.pk} заблокирован из-за отсутствия активности в течении 30-и дней")
