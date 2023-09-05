from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.database_setup import session
from lib.review import Review
from lib.database_setup import Base  # Import the Base object


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship("Review", back_populates="restaurant")
    customers = relationship("Customer", secondary="reviews")

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return self.customers

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]
