import tkinter as tk
from tkinter import ttk
from repository.general_list import read_from_file
from view.employee_report import show_employee_report
from view.product_report import show_product_report
from view.transaction_report import show_transaction_report


def show_inventory_report():
    window = tk.Tk()
    window.title("گزارش موجودی کالا")
    window.geometry("400x400")

    product_list = read_from_file("product")
    sorted_products = sorted(product_list, key=lambda product: product["name"])

    tree = ttk.Treeview(window, columns=("name", "quantity"), show="headings")
    tree.heading("name", text="نام محصول")
    tree.heading("quantity", text="تعداد")
    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    list(map(lambda product: tree.insert("", "end", values=(product["name"], product["quantity"])), sorted_products))

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="لیست کارکنان", command=show_employee_report, width=15).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="لیست محصولات", command=show_product_report, width=15).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text=" لیست تراکنش ها", command=show_transaction_report, width=15).pack(side=tk.LEFT, padx=5)

    window.mainloop()
