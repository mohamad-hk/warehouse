from model.transanction import Transaction


def show_transaction_menu():
    while True:
        print("1)Import to warehouse\n2)remove from warehouse\n3)return")
        input_user = input("Enter your option number: ")
        transaction_obj = Transaction()
        match input_user:
            case "1":
                transaction_obj.handle_transaction("import")
            case "2":
                transaction_obj.handle_transaction("export")
            case "3":
                return
            case _:
                print("your number should be between 1 and 3")
