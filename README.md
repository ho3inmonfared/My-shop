🛒 MyShop — Django E-Commerce Practice Project

MyShop is a practice e-commerce project built to learn Django step-by-step.
The project uses the MyShop Bootstrap template and includes essential online store features such as product listing, categories, and a session-based shopping cart.

🚀 Features

Category-based product browsing

Product detail pages

Add to Cart / Remove from Cart

Session-based shopping cart

Responsive UI using Bootstrap

Clean Django project structure

Admin panel for product management

🧱 Tech Stack

Python 3.x

Django 5.x

Bootstrap 5 (MyShop Template)

SQLite (default development DB)

HTML, CSS, JavaScript

📂 Project Structure
my-shop/
│── manage.py
│── config/           # Project configuration & settings
│── shop/             # Main shop application
│── static/           # Bootstrap template assets
│── requirements.txt

▶️ How to Run Locally
1️⃣ Clone the Repository
git clone firsrt
cd my-shop

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Start the Development Server
python manage.py runserver

👤 Admin Panel (Optional)

Create a superuser to manage products:

python manage.py createsuperuser


Then login at:

http://127.0.0.1:8000/admin/

📌 Project Status

This project is under active development and meant for learning Django and building an e-commerce structure from scratch.