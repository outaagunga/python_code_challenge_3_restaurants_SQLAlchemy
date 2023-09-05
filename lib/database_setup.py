from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# The URL for your database
DATABASE_URL = 'sqlite:///database.db'

# Creating a database engine
engine = create_engine(DATABASE_URL)

# Creating a Session class
Session = sessionmaker(bind=engine)

# Exporting the session object
session = Session()
