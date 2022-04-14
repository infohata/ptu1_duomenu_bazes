from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from bankas import Bankas, Saskaita, Klientas, Likutis
from tkinter import *

engine = create_engine('sqlite:///bankas_db.db')
Session = sessionmaker(bind=engine)
session = Session()

def right_l_box():
    vartotojas = left_listbox.get(left_listbox.curselection()).split()
    vart_id = int(vartotojas[2])
    print(vart_id)
    listbox_bankas = session.query(Saskaita).filter(Saskaita.klientas.personal_id == vart_id)
    print(listbox_bankas)
    right_listbox.insert(1, *listbox_bankas)

def rodyti():
    rezultatas['text'] = sarasas[left_listbox.curselection()[0]]

langas = Tk()
langas.geometry("400x200")
scrollbaras = Scrollbar(langas)
left_listbox = Listbox(langas, width=30, yscrollcommand = scrollbaras.set)
right_listbox = Listbox(langas, width=50, yscrollcommand = scrollbaras.set)
scrollbaras.config(command=left_listbox.yview)
# sarasas = []
# sarasas2 = []
sarasas = session.query(Klientas).all()
# sarasas2 = session.query(Bankas.name).filter(Bankas.customer_id == 1).all()
# sarasas3 = session.query(Saskaita).join(Bankas).filter(Saskaita.bank_id == 1).filter(Saskaita.customer_id ==2)
left_listbox.insert(0, *sarasas)
# right_listbox.insert(0,*sarasas2)
rezultatas = Listbox(langas)
but =Button(langas, text="Rodyti", command=right_l_box)

left_listbox.grid(row=0, column=0)
right_listbox.grid(row=0, column=1)
but.grid(row=1, column=1)



langas.mainloop()