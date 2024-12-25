This README provides the steps to run the Django project locally, including setting up the PostgreSQL database and installing required dependencies.

Additionally, It includes instructions for testing API Endpoints using tools like Postman or curl.

A. Django Project Setup

Prerequisites

Make sure you have the following installed:
- [Python](https://www.python.org/downloads/) (3.8+ recommended)
- [PostgreSQL](https://www.postgresql.org/download/) (latest stable version)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (optional but recommended)

Steps to Set Up the Project.

1. Clone the repository.
First, clone the project repository to your local machine.


git clone https://github.com/torddey/multi-tenants.git.
cd your-django-project.


2. i. Set up a virtual envireonment.
python -m venv venv.

ii. Activate the virtual environment.
venv\Scripts\activate (On Windows).
source venv/bin/activate (On macOS/Linux).


3. Install dependencies.
pip install -r requirements.txt.


4. Setup a PostgreSQL database.
i. Open postgresql and log into the postgresql shell:
psql -U postgres.

ii. Create new database for the project:
CREATE DATABASE your_project_db;

iii. Create new user and grant all priviledges:
CREATE USER your_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE your_project_db TO your_user;

iv. Exist postgresql: 
\q.

5. Update Database configurations in settings.py with Postgresql.

6. Apply Database MIgrations.
python manage.py makemigrations.
python manage.py migrate.

7. Create a superuser.
python manage.py createsuperuser.
Visit admin dashboard on http://localhost:8000/admin/.

8. Run the server:
python manage.py runserver.
Access the server on http://localhost:8000/ (Main app).
Visit a specific Tenant at either (nike.localhost:8000/) or (adidas.localhost:8000/).




B. API Endpoints.

Create Product: POST /api/products/

Retrieve Products: GET /api/products/

Update Product: PUT /api/products/{id}/

Delete Product: DELETE /api/products/{id}/




C. Test API Endpoints.

API Testing using Postman.
Open Postman and enter the URL:  http://nike.localhost:8000/api/products/. | http://adidas.localhost:8000/api/products/

Select the HTTP Method (GET, POST, etc.).

Send the Request and view the response in Postman.



