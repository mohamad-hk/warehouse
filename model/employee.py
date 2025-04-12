from repository.employee_list import write_to_file, read_from_file


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
        e_f_name = input("Enter first name: ")
        employee_item["first_name"] = e_f_name
        e_l_name = input("Enter last name: ")
        employee_item["last_name"] = e_l_name
        e_gender = input("Enter gender: ")
        employee_item["gender"] = e_gender
        e_birth = int(input("Enter date of birth: "))
        employee_item["date_of_birth"] = e_birth
        write_to_file(employee_item)

    def edit_employee(self):
        new_employee = {}
        employees = read_from_file()
        e_id = int(input("Enter employees id: "))
        temp_employee = list(filter(lambda employee: employee["id"] == e_id, employees))
        if not temp_employee:
            print("employee not found!")
            return
        e_name = input(f" (old first name:{temp_employee[0]["first_name"]})=>Enter new name of employee: ")
        if e_name != "":
            new_employee["first_name"] = e_name
        else:
            new_employee["first_name"] = temp_employee[0]["first_name"]

        e_l_name = input(
            f"(old last name:{temp_employee[0]["last_name"]})=> Enter new last name of employee: ")
        if e_l_name != "":
            new_employee["last_name"] = e_l_name
        else:
            new_employee["last_name"] = temp_employee[0]["last_name"]

        e_gender = input(
            f"(old gender:{temp_employee[0]["gender"]})=> Enter new gender of employee: ")
        if e_gender != "":
            new_employee["gender"] = e_gender
        else:
            new_employee["gender"] = temp_employee[0]["gender"]

        e_date_of_birth = int(
            input(f"(old quantity:{temp_employee[0]["date_of_birth"]})=> Enter new date_of_birth of employee: "))
        if e_date_of_birth != temp_employee[0]["date_of_birth"]:
            new_employee["date_of_birth"] = e_date_of_birth
        else:
            new_employee["date_of_birth"] = temp_employee[0]["date_of_birth"]

        new_employee["id"] = e_id
        employees = list(
            map(lambda employee: {**employee, **new_employee} if employee["id"] == e_id else employee, employees))

        write_to_file(employees)

    def remove_employee(self):
        employees = read_from_file()
        e_id = int(input("Enter employee id: "))
        employee_found = list(filter(lambda employee: employee["id"] == e_id, employees))
        if not employee_found:
            print("Employee not found!")
            return
        else:
            updated_employees_list = list(filter(lambda employee: employee["id"] != e_id, employees))
            write_to_file(updated_employees_list)
