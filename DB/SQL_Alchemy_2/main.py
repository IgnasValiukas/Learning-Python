# Padaryti duomenų bazės schemą (galima ją parodyti dėstytojui).
# Sukurti programą su UI konsolėje, kuri leistų įvesti asmenis, bankus, sąskaitas.
# Leistų vartotojui peržiūrėti savo sąskaitas ir jų informaciją, pridėti arba nuimti iš jų pinigų.
# Leistų bendrai peržiūrėti visus bankus, vartotojus, sąskaitas ir jų informaciją.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import User, Bank, BankAccount

engine = create_engine('sqlite:///bank_account.db')
Session = sessionmaker(bind=engine)
session = Session()


def all_users():
    users = session.query(User).all()
    for user in users:
        print(user)


def all_banks():
    banks = session.query(Bank).all()
    for bank in banks:
        print(bank)


def all_bank_accounts():
    accounts = session.query(BankAccount).all()
    for account in accounts:
        print(account)


while True:
    try:
        option = int(input(
            "OPTIONS\n1 - add user\n2 - add bank\n3 - add bank account\n4 - show users bank account\n5 - update account balance\n6 - show all data\n7 - close\nChoose option: "))
        if option == 1:
            f_name = input("First name: ")
            l_name = input("Last name: ")
            personal_code = int(input("Personal code: "))
            phone_number = input("Phone number: ")
            user_data = User(f_name=f_name, l_name=l_name, personal_code=personal_code, phone_number=phone_number)
            session.add(user_data)
            session.commit()
            print("Successfully added!\n")

        if option == 2:
            name = input("Bank name: ")
            address = input("Bank address: ")
            bank_code = int(input("Bank code: "))
            swift_code = input("SWIFT code: ")
            bank_data = Bank(name=name, address=address, bank_code=bank_code, swift_code=swift_code)
            session.add(bank_data)
            session.commit()
            print("Successfully added!\n")

        if option == 3:
            print(f'{"-" * 50}\nUsers:')
            all_users()
            print(f'{"-" * 50}\nBanks:')
            all_banks()
            print("-" * 50)
            account_number = input("Account number: ")
            account_balance = float(input("Account balance: "))
            user_id = int(input("User ID: "))
            bank_id = int(input("Bank ID: "))
            bank_account_data = BankAccount(account_number=account_number, account_balance=account_balance,
                                            user_id=user_id,
                                            bank_id=bank_id)
            session.add(bank_account_data)
            session.commit()
            print("Successfully added!\n")

        if option == 4:
            print(f'{"-" * 50}\nUsers:')
            all_users()
            print("-" * 50)
            id_choice = int(input("Select user ID whose bank account you want to see: "))
            users_id = session.get(User, id_choice)
            for acc in users_id.bank_accounts:
                print(
                    f'ID {acc.id}: {acc.account_number}, acc balance = {acc.account_balance}, user id = {acc.user_id}, bank id = {acc.bank_id}')
            print("-" * 50)

        if option == 5:
            print(f'{"-" * 50}\nUsers:')
            all_users()
            print("-" * 50)
            id_choice = int(input("Select user ID whose bank account balance you want to change: "))
            users_id = session.get(User, id_choice)
            for acc in users_id.bank_accounts:
                print(
                    f'ID {acc.id}: {acc.account_number}, acc balance = {acc.account_balance}')
            print("-" * 50)
            acc_id_choice = int(input("Select which bank account balance you want to change: "))
            acc_id = session.get(BankAccount, acc_id_choice)
            print("*" * 50)
            show_option = int(input(
                "BALANCE OPTIONS:\n1 - add money\n2 - withdraw money\nChoose option: "))
            if show_option == 1:
                add_money = int(input("How much do you want to add: "))
                added_balance = acc_id.account_balance + add_money
                acc_id.account_balance = added_balance
            if show_option == 2:
                withdraw_money = int(input("How much do you want to add: "))
                withdraw_balance = acc_id.account_balance - withdraw_money
                acc_id.account_balance = withdraw_balance
            session.commit()
            print(f'{"-" * 50}\n')

        if option == 6:
            print("*" * 50)
            show_option = int(input(
                "SHOW OPTIONS:\n1 - show all users\n2 - show all banks\n3 - show all bank account\nChoose option: "))
            if show_option == 1:
                print(f'{"-" * 50}\nUsers:')
                all_users()
                print("-" * 50)
            if show_option == 2:
                print(f'{"-" * 50}\nBanks:')
                all_banks()
                print("-" * 50)
            if show_option == 3:
                print(f'{"-" * 50}\nBank Accounts:')
                all_bank_accounts()
                print("-" * 50)
            if show_option > 3:
                print("\nWrong Input!\n")
                continue

        if option == 7:
            break

        if option > 7:
            print("\nWrong Option!\n")
    except ValueError:
        print("\nWrong Input!\n")
