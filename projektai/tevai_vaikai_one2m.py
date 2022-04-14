from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine("sqlite:///projektai/tevai_vaikai_one2m.db")
Base = declarative_base()


class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    # vaikas_id = Column(Integer, ForeignKey('vaikas.id'), nullable=True)
    vaikai = relationship("Vaikas", back_populates="tevas")


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    mokymosi_istaiga = Column("mokymosi_istaiga", String, nullable=True)
    tevas_id = Column(Integer, ForeignKey('tevas.id'), nullable=True)
    tevas = relationship("Tevas", back_populates="vaikai")


Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

## pirmas variantas
# tevas = Tevas(vardas="Tevux", pavarde="Gerulis")
# sunus = Vaikas(vardas="Sunus", pavarde="Gerulis", mokymosi_istaiga="CodeAcademy", tevas=tevas)
# dukra = Vaikas(vardas="Dukra", pavarde="Gerulele", mokymosi_istaiga="CodeAcademy", tevas=tevas)
# session.add(tevas)
# session.add(dukra)
# session.add(sunus)
# session.commit()

## antras variantas
# sunus = Vaikas(vardas="Sunus", pavarde="Gerulis", mokymosi_istaiga="CodeAcademy")
# dukra = Vaikas(vardas="Dukra", pavarde="Gerulele", mokymosi_istaiga="CodeAcademy")
# tevas = Tevas(vardas="Tevux", pavarde="Gerulis")
# tevas.vaikai.append(sunus)
# tevas.vaikai.append(dukra)
# session.add(tevas)
# session.commit()


## crUd
# tevas = session.query(Tevas).get(2)
# tevas.vaikai[1].vardas = "Dukrele"
# session.commit()

## cruD
# tevas = session.query(Tevas).get(2)
# sunus = tevas.vaikai[1]
# tevas.vaikai.remove(sunus)
# session.commit()

## cRud
tevas = session.query(Tevas).get(2)
print(tevas.vardas, tevas.pavarde)
for vaikas in tevas.vaikai:
    print("\\-", vaikas.vardas, vaikas.pavarde)

# vaikelis = Vaikas(vardas="Dukra", pavarde="Gerulele", mokymosi_istaiga="CodeAcademy")
# tevelis = Tevas(vardas="Tevas", pavarde="Gerulis", vaikas=vaikelis)
# tevelis = Tevas(vardas="Tevas", pavarde="Gerulis", vaikas=session.query(Vaikas).get(1))
# # session.add(vaikelis)
# session.add(tevelis)
# session.commit()

## cRUd
# tevux = session.query(Tevas).get(1)
# print(tevux.vaikas.vardas)
# dukrele = session.query(Vaikas).get(2)
# print(dukrele.vardas)
# tevux.vaikas = dukrele
# session.commit()
## cruD
# session.delete(tevux.vaikas)
# session.commit()
# print(tevux.vardas, tevux.vaikas)
# vaikai = session.query(Vaikas).all()
# [print(i.vardas) for i in vaikai]
