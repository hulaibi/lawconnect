# LawConnect 

**LawConnect** is a legal case management platform that connects users with lawyers. Users can submit cases, track their status, and engage in private chat communication when the case is accepted. Lawyers can review, accept, or reject cases through an intuitive dashboard.

---

##  Screenshots

### Homepage
![Homepage](static/screenshots/homepage.png)

### My Cases
![My Cases](static/screenshots/my_cases.png)

### Admin Dashboard
![Admin Dashboard](static/screenshots/admin_dashboard.png)

### Chat Interface
![Chat](static/screenshots/chat.png)

---

##  ERD - Entity Relationship Diagram

![ERD](static/screenshots/erd.png)

---

##  Features

-  User Registration & Authentication
-  Case Submission by Users
-  Admin Dashboard for Lawyers
-  Accept / Reject Cases by Status
-  Case-specific Chat when case is **In Progress**
-  Responsive UI with dark modern theme
-  Permissions and Role-based Access (User / Lawyer)

---

##  Tech Stack

| Layer        | Technology             |
|--------------|------------------------|
| Frontend     | Django, HTML, CSS      |
| Backend      | Django (Python)        |
| Database     | PostgreSQL             |
| Auth         | Django Authentication  |

---

##  How to Run the Project Locally

### 1. Clone the Repo

```bash
git clone https://github.com/hulaibi/lawconnect.git
cd lawconnect

Install dependencies:

bash
Copy
Edit
pipenv install
Activate shell:

bash
Copy
Edit
pipenv shell
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Create superuser (optional for admin dashboard):

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Access the app:

Go to http://localhost:8000


