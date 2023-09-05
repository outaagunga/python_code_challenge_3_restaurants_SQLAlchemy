# restaurant.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from your_sqlalchemy_setup import Base


class Restaurant(Base):
    # Define the Restaurant class with the necessary columns and relationships
    __tablename__ = 'restaurants'

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Relationships
    reviews = relationship("Review", back_populates="restaurant")
    customers = relationship("Customer", secondary="reviews")

    # Methods
    def reviews(self):
        # Implement the Restaurant reviews() method
        pass

    def customers(self):
        # Implement the Restaurant customers() method
        pass

    @classmethod
    def fanciest(cls):
        # Implement the Restaurant fanciest() method (class method)
        pass

    def all_reviews(self):
        # Implement the Restaurant all_reviews() method
        pass
