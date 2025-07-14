# 🎥 Transcode Nexus – Cloud & DevOps Mini Capstone Project

## 📌 Overview

**Transcode Nexus** is a cloud-hosted, Dockerized web app that allows users to upload videos in formats such as `.mp4`, `.avi`, `.mov`, `.webm` and convert them into other formats using **FFmpeg**. Built with **Flask**, served through **NGINX**, and deployed on an **AWS EC2** instance, this project demonstrates full-stack cloud deployment, DevOps practices, and video processing.

---

## 🏧 Architecture Diagram

```
User Browser
     │
     ▼
NGINX (Port 80)
     │
     ▼
Flask App (Docker, Port 3000)
     │
     ▼
FFmpeg via Python subprocess
     │
     ▼
Converted Video Output
```

---

## 🚀 Features

* Upload video files (`.mp4`, `.avi`, `.mov`, `.webm`)
* Choose desired output format
* Backend video conversion with FFmpeg
* Secure upload handling and size restriction
* Dockerized for easy deployment
* Hosted on AWS EC2 with NGINX reverse proxy

---

## 🔧 Technologies Used

| Component        | Tech Stack              |
| ---------------- | ----------------------- |
| Backend API      | Python (Flask)          |
| Video Processing | FFmpeg (via subprocess) |
| Frontend         | HTML5 + Bootstrap       |
| Containerization | Docker                  |
| Reverse Proxy    | NGINX                   |
| Hosting          | AWS EC2                 |
| Version Control  | GitHub                  |

---

## 📂 Project Structure

```
transcode-nexus/
├── app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   ├── uploads/
│   └── converted/
├── Dockerfile
├── requirements.txt
├── nginx.conf
└── README.md
```

---

## 🛠️ Setup Instructions

### 🧑‍💻 Local Testing

```bash
# Clone the repository
git clone https://github.com/nisharamary/Transcode-Nexus.git
cd transcode-nexus

# Build Docker image
docker build -t transcode-nexus .

# Run the container
docker run -d -p 5000:5000 --name converter transcode-nexus

# Access in browser
http://localhost:3000
```

---

### ☑️ Cloud Deployment (EC2 + NGINX)

1. Launch Ubuntu EC2 instance on AWS
2. Open ports: 22 (SSH), 80 (HTTP)
3. SSH into instance:

   ```bash
   ssh -i key.pem ubuntu@<public-ip>
   ```
4. Install Docker & NGINX:

   ```bash
   sudo apt update
   sudo apt install -y docker.io nginx git
   ```
5. Clone repo & build:

   ```bash
   git clone https://github.com/nisharamary/Transcode-Nexus.git
   cd transcode-nexus
   sudo docker build -t transcode-nexus .
   sudo docker run -d -p 5000:5000 --name converter transcode-nexus
   ```
6. Configure NGINX:

   ```bash
   sudo cp nginx.conf /etc/nginx/sites-available/transcode-nexus
   sudo ln -s /etc/nginx/sites-available/transcode-nexus /etc/nginx/sites-enabled/
   sudo rm /etc/nginx/sites-enabled/default
   sudo systemctl restart nginx
   ```

---

## ✅ Commands Used

### FFmpeg:

```bash
ffmpeg -i input.mp4 output.avi
```

### Docker:

```bash
docker build -t transcode-nexus .
docker run -d -p 3000:3000 --name converter transcode-nexus
```

---

## 🔐 Security Measures

* Whitelisted file types (`.mp4`, `.avi`, `.mov`, `.webm`)
* Max file size: 100MB
* Output filenames sanitized
* Docker isolation
* Optional: Auto-deletion & async processing (see below)

---

## 💡 Optional Enhancements

Students seeking bonus credit can implement:

* [ ] ✅ Async conversion with Celery + Redis
* [ ] ✅ Email notification when video is ready
* [ ] ✅ Auto-delete files after X hours (cron or scheduled job)
* [ ] ✅ Upload to Amazon S3 or cloud storage
* [ ] ✅ Video compression toggle (resolution, bitrate)

---

## 🖼️ Screenshots

*Include these screenshots before final submission:*

* [ ] Web Interface (Upload Form)
* [ ] EC2 CLI Setup (Docker + NGINX)
* [ ] Sample Converted Video File
* [ ] Architecture Diagram

---

## 🔗 GitHub Repository

[👉 View on GitHub](https://github.com/nisharamary/Transcode-Nexus.git)

---

## 👩‍🏫 Authors / Credits

* **Your Name**
* Project for: Cloud & DevOps Mini Capstone Project

