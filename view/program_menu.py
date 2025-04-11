from view.employee_menu import show_employee_menu
from view.product_menu import show_product_menu
from view.transaction_menu import show_transaction_menu


def program_menu():
    while True:
        print("1)product\n2)Employee\n3)Transaction\n4)Report\n5)Exit")
        input_user = input("Enter your option number: ")
        match input_user:
            case "1":
                show_product_menu()
            case "2":
                show_employee_menu()
            case "3":
                show_transaction_menu()
            case "4":
                pass
            case "5":
                exit()
