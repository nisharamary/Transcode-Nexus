# app/main.py
import os
from flask import request, render_template, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from app import create_app           # ✅ absolute import works when run as a module
from app.tasks import convert_video  # ✅ absolute import

app = create_app()

ALLOWED_EXTENSIONS = {"mp4", "avi", "mov", "webm", "mkv"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_video():
    if request.method == "POST":
        file = request.files.get("video")
        output_format = request.form.get("format")
        if not (file and allowed_file(file.filename) and output_format):
            return "Invalid file or format.", 400

        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(input_path)

        base = os.path.splitext(filename)[0]
        output_filename = f"{base}.{output_format}"
        output_path = os.path.join(app.config["CONVERTED_FOLDER"], output_filename)

        job = convert_video.delay(input_path, output_path, output_format)
        return render_template("queued.html", task_id=job.id)

    return render_template("index.html")

@app.route("/status/<task_id>")
def task_status(task_id):
    job = convert_video.AsyncResult(task_id)
    if job.state == "PENDING":
        response = {"state": job.state, "status": "waiting in queue…"}
    elif job.state == "SUCCESS":
        response = {"state": job.state, "output_filename": job.result["output_filename"]}
    elif job.state == "FAILURE":
        response = {"state": job.state, "error": str(job.info)}
    else:
        response = {"state": job.state, "status": str(job.info)}
    return jsonify(response)

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(app.config["CONVERTED_FOLDER"], filename, as_attachment=True)

@app.route("/debug-files")
def debug_files():
    return "<br>".join(os.listdir(app.config["CONVERTED_FOLDER"]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

