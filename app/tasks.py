# app/tasks.py
import subprocess
from pathlib import Path
from app import celery

@celery.task(bind=True)
def convert_video(self, input_path: str, output_path: str, output_format: str):
    try:
        subprocess.run(["ffmpeg", "-y", "-i", input_path, output_path], check=True)
        return {"output_filename": Path(output_path).name}
    except subprocess.CalledProcessError as exc:
        raise

