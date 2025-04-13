from controller.validate_employee import check_name, check_jalali_birthdate, check_gender
from repository.general_list import write_to_file, read_from_file


class Employee:
    def __init__(self, first_name=None, last_name=None, gender=None, date_of_birth=None, employee_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.employee_id = employee_id

    def add_employee(self):
        employee_item = {}
        e_id = 0
        employee_item["id"] = e_id

        while True:
            try:
                e_f_name = input("Enter first name: ")
                if not check_name(e_f_name):
                    raise ValueError("Enter correct first name")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                e_l_name = input("Enter last name: ")
                if not check_name(e_l_name):
                    raise ValueError("Enter correct last name")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                e_birth = input("Enter date of birth: ")
                if not check_jalali_birthdate(e_birth):
                    raise ValueError("Enter correct date of birth like --> 1400/02/30")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                e_gender = input("Enter your gender: ")
                if not check_gender(e_gender):
                    raise ValueError("Enter male or female")
                break
            except ValueError as e:
                print(e)

        employee_item["first_name"] = e_f_name
        employee_item["last_name"] = e_l_name
        employee_item["gender"] = e_gender
        employee_item["date_of_birth"] = e_birth
        write_to_file(employee_item, "employee")

    def edit_employee(self):
        new_employee = {}
        employees = read_from_file("employee")
        try:
            e_id = int(input("Enter employee id: "))
        except ValueError:
            print("Invalid id!")
            return

        temp_employee = list(filter(lambda employee: employee["id"] == e_id, employees))
        if not temp_employee:
            print("Employee not found!")
            return

        while True:
            try:
                e_name = input(f"(old first name: {temp_employee[0]['first_name']}) => Enter new first name: ")
                if e_name == "":
                    new_employee["first_name"] = temp_employee[0]["first_name"]
                    break
                if not check_name(e_name):
                    raise ValueError("Enter correct first name")
                new_employee["first_name"] = e_name
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                e_l_name = input(f"(old last name: {temp_employee[0]['last_name']}) => Enter new last name: ")
                if e_l_name == "":
                    new_employee["last_name"] = temp_employee[0]["last_name"]
                    break
                if not check_name(e_l_name):
                    raise ValueError("Enter correct last name")
                new_employee["last_name"] = e_l_name
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                e_gender = input(f"(old gender: {temp_employee[0]['gender']}) => Enter new gender: ")
                if e_gender == "":
                    new_employee["gender"] = temp_employee[0]["gender"]
                    break
                if not check_gender(e_gender):
                    raise ValueError("Enter 'male' or 'female'")
                new_employee["gender"] = e_gender
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                e_date_of_birth = input(
                    f"(old date of birth: {temp_employee[0]['date_of_birth']}) => Enter new date of birth: ")
                if e_date_of_birth == "":
                    new_employee["date_of_birth"] = temp_employee[0]["date_of_birth"]
                    break
                if not check_jalali_birthdate(e_date_of_birth):
                    raise ValueError("Enter correct date of birth like --> 1400/02/30")
                new_employee["date_of_birth"] = e_date_of_birth
                break
            except ValueError as e:
                print(e)

        new_employee["id"] = e_id
        employees = list(
            map(lambda employee: {**employee, **new_employee} if employee["id"] == e_id else employee, employees)
        )

        write_to_file(employees, "employee")

    def remove_employee(self):
        employees = read_from_file()
        e_id = int(input("Enter employee id: "))
        employee_found = list(filter(lambda employee: employee["id"] == e_id, employees))
        if not employee_found:
            print("Employee not found!")
            return
        else:
            updated_employees_list = list(filter(lambda employee: employee["id"] != e_id, employees))
            write_to_file(updated_employees_list, "employee")
