from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from lib.database_setup import session

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurants'
    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Relationships
    reviews = relationship("Review", back_populates="restaurant")
    customers = relationship("Customer", secondary="reviews")

    # Methods
    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return self.customers

    def fanciest(self):
        return session.query(Restaurant).order_by(Restaurant.price.desc()).first()

    def all_reviews(self):
        review_strings = []
        for review in self.reviews:
            review_strings.append(review.full_review())
        return review_strings
