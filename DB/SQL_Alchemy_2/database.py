# Asmuo turi vardą, pavardę, asmens kodą, tel. numerį
# Asmuo gali turėti daug sąskaitų tame pačiame arba skirtinguose bankuose
# Bankas turi pavadinimą, adresą, banko kodą, SWIFT kodą
# Sąskaita turi numerį, balansą, priskirtą asmenį ir banką

from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine('sqlite:///bank_account.db')
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    f_name = Column("first_name", String)
    l_name = Column("last_name", String)
    personal_code = Column(Integer, unique=True)
    phone_number = Column(String, unique=True)
    bank_accounts = relationship("BankAccount", back_populates="user")

    def __init__(self, f_name, l_name, personal_code, phone_number):
        self.f_name = f_name
        self.l_name = l_name
        self.personal_code = personal_code
        self.phone_number = phone_number

    def __repr__(self):
        return f"ID {self.id}: {self.f_name} {self.l_name}, {self.personal_code}, {self.phone_number}"


class Bank(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True)
    name = Column("bank_name", String)
    address = Column(String)
    bank_code = Column(String)
    swift_code = Column(String)
    bank_accounts = relationship("BankAccount", back_populates="bank")

    def __init__(self, name, address, bank_code, swift_code):
        self.name = name
        self.address = address
        self.bank_code = bank_code
        self.swift_code = swift_code

    def __repr__(self):
        return f"ID {self.id}: {self.name}, {self.address}, {self.bank_code}, {self.swift_code}"


class BankAccount(Base):
    __tablename__ = "bank_account"
    id = Column(Integer, primary_key=True)
    account_number = Column(String, unique=True)
    account_balance = Column(Float)
    user_id = Column(Integer, ForeignKey("user.id"))
    bank_id = Column(Integer, ForeignKey("bank.id"))
    user = relationship("User", back_populates="bank_accounts")
    bank = relationship("Bank", back_populates="bank_accounts")

    def __init__(self, account_number, account_balance, user_id, bank_id):
        self.account_number = account_number
        self.account_balance = account_balance
        self.user_id = user_id
        self.bank_id = bank_id

    def __repr__(self):
        return f"ID {self.id}: {self.account_number}, {self.account_balance}, {self.user_id}, {self.bank_id}"


if __name__ == '__main__':
    Base.metadata.create_all(engine)
