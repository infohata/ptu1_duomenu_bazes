from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///bankas_db.db')
Base = declarative_base()

class Bankas(Base):
    __tablename__ = 'Bankai'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("Pavadinimas", String)
    address = Column("Adresas", String)
    reg_code = Column("Kodas", Integer) 
    swift = Column("SWIFT", String)
    saskaitos = relationship('Saskaita', back_populates = 'bankas')

    def __str__(self):  
        return f"{self.name} {self.address} {self.reg_code} {self.swift}"

class Saskaita(Base):
    __tablename__ = 'Saskaitos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    acc_no = Column(String)
    bank_id = Column(Integer, ForeignKey('Bankai.id'))
    customer_id = Column(Integer, ForeignKey('Klientai.id'))
    klientas = relationship("Klientas", back_populates = 'saskaitos')
    bankas = relationship('Bankas', back_populates = 'saskaitos')
    likuciai = relationship('Likutis', back_populates = 'saskaita')

    def __str__(self):  
        return f"{self.acc_no}"

class Klientas(Base):
    __tablename__ = 'Klientai'
    id = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column(String)
    l_name = Column(String)
    personal_id = Column(Integer)
    tel_no = Column(Integer)
    saskaitos = relationship("Saskaita", back_populates = 'klientas')

    def __str__(self):  
        return f"{self.f_name} {self.l_name} {self.personal_id} {self.tel_no}"

class Likutis(Base):
    __tablename__ = 'Likuciai'
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, default = 0)
    acc_id = Column(Integer, ForeignKey('Saskaitos.id'))
    saskaita = relationship('Saskaita', back_populates = 'likuciai')


Base.metadata.create_all(engine)

    # def __init__(self, name, address, reg_code, swift):  
    #     self.name = name
    #     self.address = address
    #     self.reg_code = reg_code
    #     self.swift = swift
        
    # def __repr__(self):
    #     return f"{self.id} : {self.name} {self.address} : {self.reg_code} : {self.swift}"