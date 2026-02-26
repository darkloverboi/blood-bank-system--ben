# 🩸 Blood Bank Management System

A full-stack web application built using **Python and Flask** to manage blood donors, blood requests, and administrative operations efficiently.

🔗 **Live Demo:**  
https://blood-bank-system-ben.onrender.com/

---
## 📸 Application Screenshot

![Blood Bank System](home-dashboard.png)
https://github.com/darkloverboi/blood-bank-system--ben/blob/ef9f2c74dcc0baeba02c649e86031a6f4d7a643e/home-dashboard.png

---

## 📌 Project Overview

The Blood Bank Management System is designed to streamline:

- Donor registration  
- Blood request handling  
- Blood inventory monitoring  
- Administrative management  

This project demonstrates:

- Backend development using Flask  
- Database integration with SQLite  
- Authentication & session handling  
- CRUD operations  
- Deployment on Render  

---

## 🚀 Key Features

### 👨‍⚕️ Donor Module
- Register new blood donors
- Store donor details securely
- Search donors by blood group
- Delete donor records (Admin only)

### 🩸 Blood Request Module
- Submit blood requests
- Store patient & contact details
- View all blood requests (Admin)

### 🔐 Admin Module
- Secure admin login
- Admin dashboard
- View all registered donors
- View all blood requests
- Blood inventory summary
- Manage donor records

---

## 🛠 Tech Stack

| Technology | Usage |
|------------|--------|
| Python 3.12 | Backend logic |
| Flask | Web framework |
| SQLite | Database |
| HTML5 | Frontend structure |
| CSS3 | Styling |
| Render | Cloud deployment |

---

## 🗂 Project Structure

```
Blood-Bank-System/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── request.html
│   ├── admin_login.html
│   ├── dashboard.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/blood-bank-system.git
cd blood-bank-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not available:

```bash
pip install flask
```

### 5️⃣ Run Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000/
```

---

## 🔐 Admin Access

Default Admin Credentials:

```
Username: admin
Password: admin123
```

*(You can modify credentials inside the database or app configuration.)*

---

## 🗄 Database

- Database used: SQLite
- Database file auto-generates on first run (if configured in app.py)
- Tables include:
  - donors
  - requests
  - admin

---

## 🌍 Deployment

Hosted on **Render**

Live Link:
https://blood-bank-system-ben.onrender.com/

---

## 📸 Screenshots

You can add screenshots here like:

```
![Home Page](screenshots/home.png)
![Admin Dashboard](screenshots/dashboard.png)
```

---

## 📈 Future Improvements

- Email notification system
- SMS integration
- Blood availability tracking by units
- Role-based admin system
- Better UI/UX (Bootstrap or Tailwind)
- REST API version
- Docker containerization

---

## 👨‍💻 Author

**Shebin K Babu**  
Cybersecurity & Backend Developer  

🌐 Portfolio: (darkloverboi.space)  
📧 Email: kshebin86@gmail.com  

Project Category:  
Blue Team / SOC Simulation + Full Stack Development  

---

## 📜 License

This project is for educational and portfolio purposes.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
