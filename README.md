<img width="1024" height="1024" alt="LawConnect" src="https://github.com/user-attachments/assets/5feb01b5-662a-4ccb-8362-bab43afb56f1" />

LawConnect is a case management platform that connects clients with legal professionals. Users can submit cases in different legal categories and communicate with lawyers through a secure messaging system.

---

##  Screenshots

![Home](<img width="892" height="585" alt="home" src="https://github.com/user-attachments/assets/05597e08-1c57-4fc9-976a-889a521cb626" />
![Submit case](<img width="882" height="840" alt="submetcase" src="https://github.com/user-attachments/assets/52473040-beab-4dd4-803e-48e665daf941" />
![Dashboard](<img width="1877" height="751" alt="addmen" src="https://github.com/user-attachments/assets/a13cf4a5-ee50-4c27-896f-f9768f3207a0" />


---

##  ERD (Entity Relationship Diagram)

<img width="708" height="407" alt="Low Diagram drawio (2)" src="https://github.com/user-attachments/assets/7a791fe5-79e8-492f-acd1-e54df0792a3a" />

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


## Next Steps: Planned Future Enhancements (Stretch Goals)
Real-time Chat: Implement WebSockets (Django Channels) for instant messaging between clients and lawyers.

File Sharing: Allow secure upload and download of legal documents within each case.

Search & Filter: Advanced filtering and keyword search for cases in the admin dashboard.

Case Status Tracking: Visual progress indicators for each case stage (e.g., Submitted → In Review → Closed).

Notifications System: Email and in-app alerts for new messages, case updates, and deadlines.

Multi-language Support: Enable multiple languages to serve a broader audience.

Mobile-Friendly Enhancements: Optimize the UI for mobile-first usage.
