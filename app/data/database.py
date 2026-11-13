from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base, sessionmaker

base = declarative_base()

class Database:
    def __init__(self, database_url="sqlite:///clima_app.db"):
        self.engine = create_engine(database_url, echo=False)
        self.session = sessionmaker(bind=self.engine)
    
    def create_tables(self):
        base.metadata.create_all(self.engine)

    def create_session(self):
        return self.session()