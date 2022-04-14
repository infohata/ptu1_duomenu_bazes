from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine("sqlite:///projektai/tevai_vaikai_m2m.db")
Base = declarative_base()
# print("Visi grize rankikes op!")


association_table = Table('association', Base.metadata,
    Column('tevas_id', Integer, ForeignKey('tevas.id')),
    Column('vaikas_id', Integer, ForeignKey('vaikas.id'))
)


class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    # vaikas_id = Column(Integer, ForeignKey('vaikas.id'), nullable=True)
    vaikai = relationship("Vaikas", secondary=association_table, back_populates="tevai")


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    mokymosi_istaiga = Column("mokymosi_istaiga", String, nullable=True)
    # tevas_id = Column(Integer, ForeignKey('tevas.id'), nullable=True)
    tevai = relationship("Tevas", secondary=association_table, back_populates="vaikai")


Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

## Crud

# tetis = Tevas(vardas="Tetux", pavarde="Vardelis")
# mama = Tevas(vardas="Mamike", pavarde="Vardeliene")
# pirmas = Vaikas(vardas="Geras", pavarde="Vardelis")
# antra = Vaikas(vardas="Smagi", pavarde="Vardelyte")

# tetis.vaikai.append(pirmas)
# mama.vaikai.append(pirmas)
# mama.vaikai.append(antra)

# session.add(tetis)
# session.add(mama)
# session.commit()

## cRud

# tevas = session.query(Tevas).get(2)
# for vaikas in tevas.vaikai:
#     print(vaikas.vardas, vaikas.pavarde)

# [print(t.vardas) for t in tevas.vaikai[0].tevai]

vaikas = session.query(Vaikas).get(1)
for tevas in vaikas.tevai:
    print(tevas.vardas, tevas.pavarde)

