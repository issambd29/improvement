# الارتقاء — Islamic Self-Improvement OS

A complete Islamic self-improvement tracker with prayer tracking, Quran reading, physical fitness, knowledge, and programming goals — powered by Django + SQLite.

## Quick Start

### Windows
Double-click `setup.bat` — or run in Command Prompt:
```bat
setup.bat
```

### macOS / Linux
```bash
chmod +x setup.sh
./setup.sh
```

### Manual Setup
```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open **http://127.0.0.1:8000** in your browser.

## Features

| Page | What you track |
|------|---------------|
| 🏠 Dashboard | Overview, XP, streak, custom tasks |
| 🕌 Islamic | 5 daily prayers, Quran pages, morning/evening adhkar |
| 💪 Physical | Workout, sleep hours, water intake |
| 📚 Knowledge | Reading minutes, book pages, English practice |
| 💻 Programming | Coding sessions + Pomodoro timer |
| 📊 Stats | 30-day charts (XP, prayers, sleep, coding) |
| 🏆 Achievements | 12 unlockable achievements |
| ⚙️ Settings | Language, daily targets |

## XP System

| Action | XP |
|--------|----|
| Each prayer | +20 |
| Quran page | +10 (up to 100) |
| Morning adhkar | +15 |
| Evening adhkar | +15 |
| Workout | +50 |
| Sleep goal met | +30 |
| Water goal met | +20 |
| Reading goal | +40 |
| English (20min) | +25 |
| Coding goal | +50 |
| 4 Pomodoros | +30 |

## Stack
- **Backend**: Python 3 + Django 4.2
- **Database**: SQLite (no external DB needed)
- **Frontend**: Django templates + vanilla JS + Chart.js
- **Auth**: Django built-in authentication
- **Fonts**: Google Fonts (Amiri + Inter) — requires internet for fonts only

## Requirements
- Python 3.9+
- Internet connection (for Google Fonts & Chart.js CDN only)
