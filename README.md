# 🩺 Django Authentication & Blog System

A Django-based web application that provides a **role-based login and signup system** for **Patients** and **Doctors**, along with a **Blog Management System** where doctors can create posts and patients can view categorized health blogs.

---

## ✨ Features

### 🔐 Authentication System
- Separate signup forms for Patients and Doctors
- Signup Fields:
  - First Name, Last Name
  - Profile Picture Upload
  - Username, Email
  - Password + Password Confirmation
  - Address (Line 1, City, State, Pincode)
- Login system using Django authentication
- Role-based dashboards:
  - **Doctor Dashboard** → Manage and create blog posts
  - **Patient Dashboard** → View categorized blog posts
- Profile display showing uploaded profile picture and user info

### 🩸 Blog System
- **Categories:**
  - Health
  - Technology
  - Education
- **Doctor Features:**
  - Create, edit, and manage blog posts
  - Upload images and assign categories
  - Mark posts as drafts or publish
- **Patient Features:**
  - View published blogs categorized by topic
  - See post title, image, 15-word summary, author, and date

---

## 🧱 Tech Stack

| Component           | Technology                              |
|--------------------|----------------------------------------|
| Framework           | Django 5.2.7                            |
| Database            | SQLite (local) / PostgreSQL (Replit)  |
| Image Handling      | Pillow 11.3.0                           |
| Frontend            | HTML, CSS, Bootstrap                    |
| Concepts Used       | Custom User Model (AbstractUser), Forms, Decorators, Template Inheritance |

---

## 🗂 Project Structure
Login-Signup-User/
│
├── accounts/ # Authentication (User registration, login)
├── blog/ # Blog system (Categories, Posts)
├── medauth_project/ # Main Django configuration
├── media/ # Uploaded profile/blog images
├── templates/ # Base and dashboard templates
├── manage.py
└── requirements.txt


---

## ⚙️ Database Models

- **CustomUser** — Extends AbstractUser with:
  - `user_type` (Patient/Doctor)
  - Address fields
  - Profile picture
- **Category** — Predefined health categories
- **BlogPost** — Title, image, category, summary, content, author, draft flag

---

## 🧩 Key Implementation Details

- Role-based redirection after login
- `@login_required` decorators for route protection
- Blog management directly integrated into dashboards
- Default categories initialized automatically
- Summary truncation helper for blog cards

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

### 📥 Installation Steps

1. **Clone the Repository**

```bash
git clone https://github.com/Adityarawat01/Login-Signup-User.git
cd Login-Signup-User


Create and Activate Virtual Environment

Windows:

python -m venv venv
.\venv\Scripts\activate


macOS/Linux:

python3 -m venv venv
source venv/bin/activate


Install Required Libraries

pip install -r requirements.txt


Apply Migrations

python manage.py migrate


Create a Superuser

python manage.py createsuperuser


Run the Server

python manage.py runserver 5000


Open in Browser
http://127.0.0.1:5000/

🧰 Environment Configuration

If using PostgreSQL (e.g., on Replit), update settings.py:

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://<username>:<password>@<host>/<dbname>'
    )
}
