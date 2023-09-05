# customer.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from your_sqlalchemy_setup import Base


class Customer(Base):
    # Define the Customer class with the necessary columns and relationships
    __tablename__ = 'customers'

    # Columns
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Relationships
    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Restaurant", secondary="reviews")

    # Methods
    def reviews(self):
        # Implement the Customer reviews() method
        pass

    def restaurants(self):
        # Implement the Customer restaurants() method
        pass

    def full_name(self):
        # Implement the Customer full_name() method
        pass

    def favorite_restaurant(self):
        # Implement the Customer favorite_restaurant() method
        pass

    def add_review(self, restaurant, rating):
        # Implement the Customer add_review() method
        pass

    def delete_reviews(self, restaurant):
        # Implement the Customer delete_reviews() method
        pass
