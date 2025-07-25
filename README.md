# ⚖ LawConnect

LawConnect is a case management platform that connects clients with legal professionals. Users can submit cases in different legal categories and communicate with lawyers through a secure messaging system.

---

##  Screenshots

| Submit Case | Chat System | Admin Dashboard |
|-------------|-------------|-----------------|
| ![Submit Case](screenshots/submit_case.png) | ![Chat](screenshots/chat.png) | ![Dashboard](screenshots/admin_dashboard.png) |

---

##  ERD (Entity Relationship Diagram)

![ERD](screenshots/erd.png)

---

##  Features

- User authentication (client and admin)
- Submit, update, and delete cases
- Admin dashboard to manage cases
- Secure chat system per case
- Responsive design with clean lawyer-style theme (dark, gray, royal black)

---

##  Tech Stack

- **Backend**: Django + PostgreSQL
- **Frontend**: HTML + CSS (custom dark theme)
- **Auth**: Django built-in authentication
- **Env**: Pipenv

---

##  How to Run Locally (Using Pipenv)

1. **Clone the repo:**

   ```bash
   git clone https://github.com/your-username/lawconnect.git
   cd lawconnect
   ```

2. **Install dependencies:**

   ```bash
   pipenv install
   ```

3. **Activate shell:**

   ```bash
   pipenv shell
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional for admin dashboard):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the app:**

   Go to [http://localhost:8000](http://localhost:8000)

---

## Author

Hasan Hulaibi — [@hulaibi](https://github.com/hulaibi)

---

##  License

This project is for educational/demo purposes at General Assembly Bootcamp.
