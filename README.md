#  Company API - Django REST Framework

A simple and clean Django REST Framework project to manage companies using API endpoints.

---

##  About

This project is built with **Django 5** and **Django REST Framework**. It allows CRUD operations (Create, Read, Update, Delete) on company records. It’s structured to be modular, scalable, and beginner-friendly — perfect for API-based applications or integration with frontend/mobile apps.

---

##  Features

-  List all companies
-  Create new company entries
-  Edit existing company data
-  Delete company records
-  RESTful API endpoints

---

##  Technologies Used

-  Python 3
-  Django 5
-  Django REST Framework
-  SQLite (Default Database)

---

##  Project Structure

```
companyapi/
│
├── api/                  → App with models, views, serializers, urls
├── companyapi/           → Project settings and configurations
├── db.sqlite3            → SQLite Database
├── manage.py             → Django CLI
└── requirements.txt      → Python package dependencies
```

---

##  Setup Instructions

Follow these simple steps to run the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/tayyaba505/tayyaba-innovaxel-himar.git
   cd tayyaba-innovaxel-himar
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access API**
   ```
   http://127.0.0.1:8000/api/v1/companies/
   ```

---

##  API Endpoints

| Method | Endpoint                   | Description            |
|--------|----------------------------|------------------------|
| GET    | `/api/v1/companies/`       | List all companies     |
| POST   | `/api/v1/companies/`       | Add new company        |
| GET    | `/api/v1/companies/<id>/`  | Get a specific company |
| PUT    | `/api/v1/companies/<id>/`  | Update company         |
| DELETE | `/api/v1/companies/<id>/`  | Delete company         |

---

##  Author

**Tayyaba Himar**  
[GitHub: @tayyaba505](https://github.com/tayyaba505)  
 *Innovaxel Assessment Submission*

---

##  License

This project is open-source and free to use for educational purposes.

