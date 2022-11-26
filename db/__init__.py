from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from settings import DATABASE_URL

from db.models import Base


engine = create_engine(DATABASE_URL)
Session = sessionmaker(engine)

session = Session()
