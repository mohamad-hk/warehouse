from model.employee import Employee


def show_employee_menu():
    while True:
        print("1)Add employee\n2)Edit employee\n3)Remove employee\n4)return")
        input_user = input("Enter your option number: ")
        employee_obj = Employee()
        match input_user:
            case "1":
                employee_obj.add_employee()
            case "2":
                employee_obj.edit_employee()
            case "3":
                employee_obj.remove_employee()
            case "4":
                return
            case _:
                print("your number should be between 1 and 4")
