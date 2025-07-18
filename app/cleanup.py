# app/cleanup.py

import os
import time
from pathlib import Path
from app import celery
import datetime

@celery.task
def delete_old_files():
    delete_after = int(os.getenv("DELETE_AFTER_HOURS", 24))
    cutoff = time.time() - delete_after * 3600

    folders = ["/app/uploads", "/app/converted"]

    for folder in folders:
        for f in Path(folder).glob("*"):
            if f.is_file() and f.stat().st_mtime < cutoff:
                f.unlink()
