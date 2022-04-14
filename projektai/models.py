from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///projektai/projektai.db')
Base = declarative_base()


class Projektas(Base):
    __tablename__ = 'Projektas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    price = Column("price", Float)
    created_at = Column("created_at", DateTime, default=datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f"{self.id} | {self.name} | {self.price:,.2f} | {self.created_at}"


Base.metadata.create_all(engine)
