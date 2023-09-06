# python_code_challenge_3_restaurants_SQLAlchemy

Restaurant Review System

Overview
This project is a Restaurant Review System that allows users to add and manage restaurant reviews. It includes three main classes: Restaurant, Review, and Customer, each with their respective methods and relationships.

Problem Statement
The goal of this project is to create a system where customers can leave reviews for restaurants, and the system can provide useful information such as a customer's favorite restaurant, the fanciest restaurant, and more.

Project Structure
The project is organized as follows:

app.py: Contains the main application logic and SQLAlchemy setup.
models.py: Defines the Restaurant, Review, and Customer classes with their relationships and methods.
debug.py: A helper script to test the functionality of the methods before deployment.
Pipfile: Specifies project dependencies.

Getting Started
To use this project, follow these steps:

Fork the Repository
Go to the GitHub repository: Your Repository URL.
Click the "Fork" button in the upper right corner to create a copy of the repository in your GitHub account.

Clone the Repository
Open your terminal or command prompt.
Navigate to the directory where you want to clone the project.

Run the following command, replacing <your-github-username> with your actual GitHub username:

git clone https://github.com/yourusername/restaurant-review-system.git

Install Dependencies
Navigate to the project directory:
cd restaurant-review-system
Install project dependencies using Pipenv:
pipenv install

Database Setup
Make sure you have a PostgreSQL database set up.
Configure the database connection in app.py:

DATABASE_URI = 'postgresql://username:password@localhost/database_name'
Run the Application
Activate the virtual environment:

pipenv shell
Create and apply the database migrations:

flask db init
flask db migrate
flask db upgrade
Run the application:

python app.py
Usage
Once the application is running, you can interact with it using the provided classes and methods. For example:
from models import Customer, Restaurant, Review

# Create sample instances and perform operations

customer = Customer(first_name="John", last_name="Doe")
restaurant = Restaurant(name="Sample Restaurant", price=3)
customer.add_review(restaurant, 4)
restaurant.all_reviews()
Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository to your GitHub account.
Create a new branch for your feature or bug fix.
Make your changes and commit them to your branch.
Push your changes to your forked repository.
Create a pull request to the original repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.
