from .models import Log
from datetime import datetime
from django.utils import timezone


def actionlog(action):
    record = Log(event=action, event_date=datetime.now(tz=timezone.utc))
    record.save()