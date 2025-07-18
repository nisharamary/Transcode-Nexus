from celery.schedules import crontab

beat_schedule = {
    'cleanup-every-hour': {
        'task': 'app.cleanup.delete_old_files',
        'schedule': crontab(minute=0, hour='*'),
    },
}

timezone = 'UTC'
