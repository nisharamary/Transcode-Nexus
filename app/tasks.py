# tasks.py
import os
from celery import Celery
from werkzeug.utils import secure_filename
from pathlib import Path
import subprocess
from mailer import send_done_mail

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:7379")

celery = Celery(
    "video_converter",
    broker=REDIS_URL,
    backend=REDIS_URL,
    result_expires=3600,   # 1 h
)

@celery.task(bind=True)
def convert_video(self, input_path: str, output_path: str, output_format: str):
    """
    Async Celery task that wraps FFmpeg.
    Updates task state on progress (optional).
    """
    try:
        cmd = ["ffmpeg", "-y", "-i", input_path, output_path]
        subprocess.run(cmd, check=True)
        return {"output_filename": Path(output_path).name}
    except subprocess.CalledProcessError as exc:
        self.update_state(state="FAILURE", meta={"exc": str(exc)})
        raise

        