# review.py

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from your_sqlalchemy_setup import Base


class Review(Base):
    # Define the Review class with the necessary columns and relationships
    __tablename__ = 'reviews'

    # Columns
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    rating = Column(Integer)

    # Relationships
    restaurant = relationship("Restaurant")
    customer = relationship("Customer")

    # Methods
    def customer(self):
        # Implement the Review customer() method
        pass

    def restaurant(self):
        # Implement the Review restaurant() method
        pass

    def full_review(self):
        # Implement the Review full_review() method
        pass
