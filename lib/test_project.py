from lib.restaurant import Restaurant
from lib.customer import Customer
from lib.review import Review


def test_restaurant_price():
    restaurant = Restaurant(name="Test Restaurant", price=4)
    assert restaurant.price == 4


def test_customer_full_name():
    customer = Customer(first_name="Test", last_name="Customer")
    assert customer.full_name() == "Test Customer"


def test_review_rating():
    restaurant = Restaurant(name="Test Restaurant", price=3)
    customer = Customer(first_name="Test", last_name="Customer")
    review = customer.add_review(restaurant, rating=5)
    assert review.rating == 5
