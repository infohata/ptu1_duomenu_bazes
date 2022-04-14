from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Projektas


engine = create_engine('sqlite:///projektai/projektai.db')
# Session = sessionmaker(bind=engine)
# session = Session()
session = sessionmaker(bind=engine)()

## CRUD | Create Read Update Delete
## Crud | Create
# projetas3 = Projektas("Monstrinis", 50_000_000)
# session.add(projetas3)
# session.commit()

## cRud | Read su get()
# pirmas = session.query(Projektas).get(1)
# print(pirmas.name, pirmas.price)

## cRud | Read su filter() ir one() metodai
trecias = session.query(Projektas).filter_by(name="Monstrinis").one()
# print(trecias)

## cRud | Read su all()
visi = session.query(Projektas).all()
# for projektas in visi:
#     print(projektas)

## cRud | filter() ipatumai
search = session.query(Projektas).filter(Projektas.price >= 1_000)
search2 = session.query(Projektas).filter(Projektas.name.ilike("%ktas"))
search3 = session.query(Projektas).filter(
    Projektas.name.ilike("%ktas"),
    Projektas.price > 1999,
)
# [print(i) for i in search3]

## crUd | Update
# irasas = search3.first()
# irasas.price = 50_000
# session.commit()

## cruD | Delete
# session.delete(search2.first())
# session.commit()
leftovers = session.query(Projektas).all()
print(leftovers)
