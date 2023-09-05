from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from lib.database_setup import session
from review import Review
from restaurant import Restaurant


Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    # Columns
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Relationships
    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Restaurant", secondary="reviews")

    # Methods
    def get_reviews(self):
        # Return a collection of all the reviews that the customer has left
        return self.reviews

    def get_restaurants(self):
        return self.restaurants

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        return session.query(Restaurant).join(Review).filter(
            Review.customer == self
        ).order_by(Review.rating.desc()).first().get_restaurant()

    def add_review(self, restaurant, rating):
        review = Review(restaurant=restaurant, customer=self, rating=rating)
        session.add(review)
        session.commit()

    def delete_reviews(self, restaurant):
        session.query(Review).filter(
            Review.customer == self,
            Review.restaurant == restaurant
        ).delete()
        session.commit()
