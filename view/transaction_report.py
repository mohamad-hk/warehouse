import tkinter as tk
from tkinter import ttk
from repository.general_list import read_from_file


def show_transaction_report():
    window = tk.Tk()
    window.title(" لیست تراکنش ها ")

    transaction_list = read_from_file("transaction")
    tree = ttk.Treeview(window, columns=("product_name", "quantity", "status", "modified_by",),
                        show="headings")
    tree.heading("product_name", text="نام محصول")

    tree.heading("quantity", text="تعداد ")
    tree.heading("status", text="وضعیت")
    tree.heading("modified_by", text=" تغییر داده شده توسط")

    list(map(lambda transaction: tree.insert("", "end", values=(
        transaction["product_name"],
        transaction["quantity"],
        transaction["status"],
        transaction["modified_by"]
    )), transaction_list))

    tree.pack(expand=True, fill=tk.BOTH)

    window.mainloop()
