from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.database_setup import session
from lib.review import Review
from lib.restaurant import Restaurant


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Restaurant", secondary="reviews")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Fix the query to select the restaurant with the highest rating
        favorite_review = session.query(Review).filter(
            Review.customer == self
        ).order_by(Review.rating.desc()).first()
        if favorite_review:
            return favorite_review.restaurant
        else:
            return None

    def add_review(self, restaurant, rating):
        try:
            review = Review(restaurant=restaurant,
                            customer=self, rating=rating)
            session.add(review)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

    def delete_reviews(self, restaurant):
        session.query(Review).filter(
            Review.customer == self,
            Review.restaurant == restaurant
        ).delete()
        session.commit()
