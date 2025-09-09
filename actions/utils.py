# Creating a simple method to create action objects.
import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from .models import Action


def create_action(user, verb, target=None):
    # Check the action that happened in the last one minute.
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(
        user=user.id, verb=verb, created__gte=last_minute
    )
    if target:
        target_ct = ContentType.get_object_for_this_type(target)
        similar_actions = Action.objects.filter(user_id=user.id, target_ct=target_ct, target_id=)
    action = Action(user=user, verb=verb, target=target)
    action.save()
