A. To run the project locally, follow these steps:

1. Set up the virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2. Install requirements:
pip install -r requirements.txt

3. Run the server:
python manage.py runserver
Visit http://localhost:8000 to interact with the application.



B. Test the API Endpoints
You can now use tools like Postman or cURL to test the API:

Create Product: POST /api/products/
Retrieve Products: GET /api/products/
Update Product: PUT /api/products/{id}/
Delete Product: DELETE /api/products/{id}/
