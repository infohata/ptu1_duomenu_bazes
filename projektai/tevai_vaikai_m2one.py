from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine("sqlite:///projektai/tevai_vaikai.db")
Base = declarative_base()


class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    vaikas_id = Column(Integer, ForeignKey('vaikas.id'), nullable=True)
    vaikas = relationship("Vaikas")


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    mokymosi_istaiga = Column("mokymosi_istaiga", String, nullable=True)


Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

# vaikelis = Vaikas(vardas="Dukra", pavarde="Gerulele", mokymosi_istaiga="CodeAcademy")
# tevelis = Tevas(vardas="Tevas", pavarde="Gerulis", vaikas=vaikelis)
# tevelis = Tevas(vardas="Tevas", pavarde="Gerulis", vaikas=session.query(Vaikas).get(1))
# # session.add(vaikelis)
# session.add(tevelis)
# session.commit()

## cRUd
tevux = session.query(Tevas).get(1)
# print(tevux.vaikas.vardas)
# dukrele = session.query(Vaikas).get(2)
# print(dukrele.vardas)
# tevux.vaikas = dukrele
# session.commit()
## cruD
# session.delete(tevux.vaikas)
# session.commit()
print(tevux.vardas, tevux.vaikas)
vaikai = session.query(Vaikas).all()
[print(i.vardas) for i in vaikai]
