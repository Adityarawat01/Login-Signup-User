# 🩺 Login Signup User  

A Django-based authentication system with **role-based login and signup** functionality for **Patients** and **Doctors**. After signup, users are redirected to their respective dashboards with profile picture and details.  

---

## ✨ Features  

- **User Registration**: Patients and Doctors can register separately  
- **Signup Form Fields**:  
  - First Name, Last Name  
  - Profile Picture Upload  
  - Username, Email  
  - Password + Password Confirmation  
  - Address (line 1, city, state, pincode)  
- **Secure Login** using Django authentication  
- **Role-Based Dashboards**: Redirects users to Patient or Doctor dashboard  
- **Profile Display**: Shows uploaded profile picture and user details  

---

## 🛠 Tech Stack  

- **Framework**: Django `5.2.7`  
- **Database**: SQLite (default for development)  
- **Image Handling**: Pillow `11.3.0`  
- **Concepts Used**:  
  - Custom User Model (`AbstractUser`)  
  - Django Forms with validation  
  - `@login_required` decorators for access control  
  - Media handling for profile picture uploads  
  - Template inheritance (base.html → signup/login/dashboard)  

---

## 🚀 Getting Started  

Follow the steps below to install dependencies and run the server locally.  

---

### ✅ Prerequisites  

- Python **3.x**  
- pip (Python package manager)  
- Virtual environment (recommended)  

---

### 📥 Installation  

**Clone the Repository**  

```bash
git clone https://github.com/Adityarawat01/Login-Signup-User.git
cd Login-Signup-User

1. Create and Activate Virtual Environment

# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

2. Install Required Libraries

pip install -r requirements.txt

3. Database Setup

python manage.py migrate

4. Create Admin User

python manage.py createsuperuser

5. Run the Server

python manage.py runserver 5000

👉 Open in browser: http://127.0.0.1:5000/