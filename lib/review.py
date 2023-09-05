from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from lib.restaurant import Restaurant
from lib.customer import Customer
from lib.database_setup import session, Base


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    rating = Column(Integer)

    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.rating} stars"
