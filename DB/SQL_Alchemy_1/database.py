# Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba (automatiskai)

import datetime
from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///employees.db')
Base = declarative_base()


class Employee(Base):
    __tablename__ = 'Employee'
    id = Column(Integer, primary_key=True)
    f_name = Column("first_name", String)
    l_name = Column("last_name", String)
    birth_date = Column(Date)
    position = Column(String)
    salary = Column(Float)
    working_since = Column(Date, default=datetime.datetime.now)

    def __init__(self, f_name, l_name, birth_date, position, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.birth_date = birth_date
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"id: {self.id} | {self.f_name} {self.l_name}, {self.birth_date}, {self.position}, {self.salary} EUR, {self.working_since}"


Base.metadata.create_all(engine)
