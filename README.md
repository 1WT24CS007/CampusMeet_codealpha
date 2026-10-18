# CampusMeet — Real-Time Communication & Collaboration App

## 📌 Project Overview

CampusMeet is a web-based video conferencing and collaboration application developed as part of **CodeAlpha Task 4: Real-Time Communication App**. It enables authenticated users to communicate through video and audio calls while collaborating using screen sharing, file sharing, and a shared whiteboard.

## ✨ Features

- **User Authentication:** Secure login and access for registered users.
- **Real-Time Video Calling:** Communicate with other meeting participants using audio and video.
- **Microphone and Camera:** Control microphone and camera during meetings.
- **Screen Sharing:** Share your screen with other participants.
- **File Sharing:** Upload and download files within a meeting.
- **Collaborative Whiteboard:** Draw and share ideas with meeting participants.
- **WebSocket Communication:** Exchange real-time signaling and collaboration events.

## 🛠️ Technologies Used

- Python
- Django
- Django Channels
- Django ASGI / Daphne
- HTML5
- CSS3
- JavaScript
- WebRTC
- WebSockets
- SQLite

## 📂 Project Structure

```text
CampusChat/
├── campuschat/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
├── chat/
│   ├── templates/
│   │   └── meeting.html
│   ├── meeting_consumers.py
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   └── views.py
├── media/
├── manage.py
├── db.sqlite3
└── README.md
```

*Note: The structure above highlights the main files; your actual project may contain additional files.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd CampusChat
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

Install the packages used by your project, including Django, Channels, and Daphne. If you have a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

If you do not have a requirements file, install the packages listed in your project setup and create one after verifying your environment.

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

### 6. Open CampusMeet

Visit:

```text
http://127.0.0.1:8000/
```

Log in with a registered account and open a meeting room.

## 🧪 Testing

Test the application with two authenticated users and, ideally, two separate devices or computers.

- Verify that both participants can join the same meeting.
- Check video and audio in both directions.
- Test microphone mute and camera controls.
- Verify screen sharing.
- Upload and download a file.
- Draw on the whiteboard and confirm that the other participant sees the changes.
- Refresh one participant's page and verify that the meeting reconnects as expected.

## 🔐 Security Notes

- Keep Django's `SECRET_KEY` private.
- Set `DEBUG = False` and configure appropriate allowed hosts before production deployment.
- Use HTTPS and secure WebSocket connections (`wss://`) in production.
- Restrict file uploads by size and validate uploaded content.
- Do not commit passwords, secret keys, local databases containing personal information, or private uploaded files to a public repository.
- Configure authentication and meeting access controls appropriately before deploying publicly.

## 🚀 Future Enhancements

- Add a microphone and camera device selector.
- Improve meeting reconnection and participant status indicators.
- Add meeting scheduling and invitation links.
- Improve file validation and storage.
- Deploy the application to a production server with HTTPS.

## 👨‍💻 Project Information

**Project Name:** CampusMeet  
**Project Type:** Real-Time Communication and Collaboration Web Application  
**Internship Task:** CodeAlpha Task 4

Author

Chaitanya

## 📄 License

Add a license if you intend to distribute or reuse this project publicly.
