from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from lib.database_setup import session

Base = declarative_base()


class Review(Base):
    __tablename__ = 'reviews'
    # columns
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    rating = Column(Integer)

    # Relationships
    restaurant = relationship("Restaurant")
    customer = relationship("Customer")

    # Methods
    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.rating} stars"
