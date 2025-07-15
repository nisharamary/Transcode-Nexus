# app/__init__.py
from flask import Flask
from celery import Celery
import os

celery = Celery(
    __name__,
    broker=os.getenv("REDIS_URL", "redis://redis:6379"),
    backend=os.getenv("REDIS_URL", "redis://redis:6379"),
    result_expires=3600,
)

def create_app():
    app = Flask(__name__)

    # Use correct container paths
    upload_folder = "/app/uploads"
    converted_folder = "/app/converted"

    # Ensure directories exist
    os.makedirs(upload_folder, exist_ok=True)
    os.makedirs(converted_folder, exist_ok=True)

    # Update config
    app.config['UPLOAD_FOLDER'] = upload_folder
    app.config['CONVERTED_FOLDER'] = converted_folder
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB

    return app

