# DataSnap

A lightweight Google Forms alternative built with Flask and Firebase. Create public forms in a few clicks and collect responses in real time.

🔗 **Live Demo:** [https://datasnap.onrender.com](https://datasnap.onrender.com)

📦 **Repository:** [https://github.com/sheikhwasimuddin/DataSnap](https://github.com/sheikhwasimuddin/DataSnap)

## Features

- **User Authentication** — Sign up, log in, and password reset via Firebase Auth with email verification
- **Form Builder** — Create and edit forms with custom fields from a dashboard
- **Public Sharing** — Each form gets a unique public URL anyone can submit
- **Response Collection** — Submissions are stored in Firebase Realtime Database with timestamps
- **Toggle Responses** — Enable or disable form submissions at any time
- **Admin Dashboard** — View and manage all your forms in one place
- **Form Deletion** — Remove forms you no longer need

## Tech Stack

| Layer     | Technology                  |
|-----------|-----------------------------|
| Backend   | Flask, Gunicorn             |
| Database  | Firebase Realtime Database  |
| Auth      | Firebase Authentication     |
| Frontend  | Jinja2 Templates, HTML/CSS  |
| Hosting   | Render                      |

## Project Structure

```
├── app.py                 # Main Flask application and routes
├── definitions.py         # Day/month name mappings
├── wsgi.py                # WSGI entry point
├── build.sh               # Render build script
├── requirements.txt       # Python dependencies
├── templates/             # Jinja2 HTML templates
│   ├── index.html         # Login page
│   ├── signup.html        # Registration page
│   ├── dashboard.html     # User dashboard
│   ├── form.html          # Public form view
│   ├── temp_form.html     # Form editor
│   └── ...
└── static/                # Static assets
```

## Setup

### Prerequisites

- Python 3.11+
- A Firebase project with Realtime Database and Authentication enabled

### Environment Variables

Create a `.env` file in the project root:

```env
FIREBASE_APIKEY=your_api_key
FIREBASE_AUTHDOMAIN=your_project.firebaseapp.com
FIREBASE_DATABASEURL=https://your_project.firebaseio.com
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_STORAGE_BUCKET=your_project.appspot.com
FIREBASE_MESSAGING_SENDER_ID=your_sender_id
FIREBASE_APP_ID=your_app_id
FIREBASE_MEASUREMENT_ID=your_measurement_id
SESSION_SECRET_KEY=your_secret_key
```

### Local Development

```bash
pip install -r requirements.txt
python wsgi.py
```

The app will run at `http://localhost:5000`.

### Deploy to Render

1. Push the repo to GitHub
2. Create a new **Web Service** on [Render](https://render.com)
3. Set the following:
   - **Build Command:** `chmod +x build.sh && ./build.sh`
   - **Start Command:** `gunicorn app:app`
4. Add all environment variables from the `.env` section above
5. Deploy

## License

This project is open source.

## Author

Made by [sheikhwasimuddin](https://github.com/sheikhwasimuddin)
