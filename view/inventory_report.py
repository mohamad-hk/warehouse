import tkinter as tk
from tkinter import ttk
from repository.general_list import read_from_file


def show_inventory_report():
    window = tk.Tk()
    window.title("گزارش موجودی کالا")

    product_list = read_from_file("product")

    sorted_products = sorted(product_list, key=lambda product: product["name"])

    tree = ttk.Treeview(window, columns=("name", "quantity"), show="headings")

    tree.heading("name", text="نام محصول")
    tree.heading("quantity", text="تعداد")

    for product in sorted_products:
        tree.insert("", "end", values=(product["name"], product["quantity"]))

    tree.pack(expand=True, fill=tk.BOTH)

    window.mainloop()
