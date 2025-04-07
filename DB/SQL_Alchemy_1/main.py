# Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
# Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import session_user

from database import Employee
from datetime import datetime

engine = create_engine('sqlite:///employees.db')
Session = sessionmaker(bind=engine)
session = Session()

def all_employees():
    employees = session.query(Employee).all()
    for employee in employees:
        print(employee)

while True:
    option = int(input("OPTIONS\n1 - add new employee\n2 - show all employee\n3 - delete employee\n4 - update employee data\nChoose option: "))
    if option == 1:
        f_name = input("First name: ")
        l_name = input("Last name: ")
        birth_date = input("Birth date (yyyy-mm-dd): ")
        date_format = '%Y-%m-%d'
        date = datetime.strptime(birth_date, date_format)
        position = input("Job position: ")
        salary = float(input("Job salary: "))
        employee_data = Employee(f_name, l_name, date, position, salary)
        session.add(employee_data)
        session.commit()

    if option == 2:
        print("-"*100)
        all_employees()
        print("-" * 100)

    if option == 3:
        print("-" * 100)
        all_employees()
        print("-" * 100)
        id_choice = int(input("Select the employee ID you want to delete: "))
        employee_deletion = session.get(Employee, id_choice)
        session.delete(employee_deletion)
        session.commit()

    if option == 4:
        print("-" * 100)
        all_employees()
        print("-" * 100)
        id_choice = int(input("Select the employee ID you want to update: "))
        employee_update = session.get(Employee, id_choice)
        updates = int(input("UPDATE OPTIONS:\n1 - First name\n2 - Last name\n3 - Birth date\n4 - Position\n5 - Salary\nChoose option: "))
        if updates == 1:
            employee_update.f_name = input("First name:")
        if updates == 2:
            employee_update.l_name = input("Last name:")
        if updates == 3:
            birth_date = input("Birth date (yyyy-mm-dd): ")
            date_format = '%Y-%m-%d'
            date = datetime.strptime(birth_date, date_format)
            employee_update.birth_date = date
        if updates == 4:
            employee_update.position = input("Position:")
        if updates == 5:
            employee_update.salary = float(input("Salary:"))
        session.commit()