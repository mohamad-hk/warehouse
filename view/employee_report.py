import tkinter as tk
from tkinter import ttk
from repository.general_list import read_from_file


def show_employee_report():
    window = tk.Tk()
    window.title(" لیست کارکنان ")

    employee_list = read_from_file("employee")
    tree = ttk.Treeview(window, columns=("id", "first_name", "last_name", "gender", "date_of_birth"),
                        show="headings")
    tree.heading("id", text="شناسه")

    tree.heading("first_name", text="نام ")
    tree.heading("last_name", text="نام خانوادگی")
    tree.heading("gender", text="جنسیت")
    tree.heading("date_of_birth", text="تاریخ تولد")

    for employee in employee_list:
        tree.insert("", "end", values=(
            employee["id"], employee["first_name"], employee["last_name"], employee["gender"],
            employee["date_of_birth"],
        ))

    tree.pack(expand=True, fill=tk.BOTH)

    window.mainloop()
