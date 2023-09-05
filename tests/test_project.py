from lib.database_setup import engine, session
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

    # Add a review and check the rating
    review = customer.add_review(restaurant, rating=5)
    assert review.rating == 5

    # Add another review and check the rating
    review2 = customer.add_review(restaurant, rating=4)
    assert review2.rating == 4


def test_favorite_restaurant():
    restaurant1 = Restaurant(name="Restaurant A", price=3)
    restaurant2 = Restaurant(name="Restaurant B", price=2)
    customer = Customer(first_name="Test", last_name="Customer")

    # Add reviews for two restaurants
    customer.add_review(restaurant1, rating=5)
    customer.add_review(restaurant2, rating=4)

    # Check if the favorite restaurant is Restaurant A
    favorite = customer.favorite_restaurant()
    assert favorite == restaurant1


def test_delete_reviews():
    restaurant = Restaurant(name="Test Restaurant", price=3)
    customer = Customer(first_name="Test", last_name="Customer")

    # Add a review
    customer.add_review(restaurant, rating=5)

    # Delete the review
    customer.delete_reviews(restaurant)

    # Check if the review was deleted
    assert len(customer.get_reviews()) == 0


if __name__ == "__main__":
    test_restaurant_price()
    test_customer_full_name()
    test_review_rating()
    test_favorite_restaurant()
    test_delete_reviews()
    print("All tests passed!")
