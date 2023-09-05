from lib.database_setup import engine, session
from lib.restaurant import Restaurant
from lib.customer import Customer
from lib.review import Review


def main():
    # Create tables if they don't exist
    Restaurant.__table__.create(bind=engine, checkfirst=True)
    Customer.__table__.create(bind=engine, checkfirst=True)
    Review.__table__.create(bind=engine, checkfirst=True)

    # Creating some examples of data
    restaurant1 = Restaurant(name="Restaurant A", price=3)
    restaurant2 = Restaurant(name="Restaurant B", price=2)
    customer1 = Customer(first_name="John", last_name="Doe")
    customer2 = Customer(first_name="Jane", last_name="Smith")

    # Adding exaple reviews
    customer1.add_review(restaurant1, rating=4)
    customer1.add_review(restaurant2, rating=5)
    customer2.add_review(restaurant1, rating=3)

    # Querying and print the data added
    print("All Restaurants:")
    all_restaurants = session.query(Restaurant).all()
    for restaurant in all_restaurants:
        print(f"{restaurant.name}, Price: {restaurant.price}")

    print("\nAll Customers:")
    all_customers = session.query(Customer).all()
    for customer in all_customers:
        print(f"Customer: {customer.full_name()}")

    print("\nCustomer Reviews:")
    for customer in all_customers:
        print(f"{customer.full_name()}'s Reviews:")
        for review in customer.get_reviews():
            print(f"- {review.full_review()}")

    # Example to find the fanciest restaurant
    fanciest_restaurant = restaurant1.fanciest()
    print(f"\nFanciest Restaurant: {fanciest_restaurant.name}")


if __name__ == "__main__":
    main()
