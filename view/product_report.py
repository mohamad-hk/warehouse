import tkinter as tk
from tkinter import ttk
from repository.general_list import read_from_file


def show_product_report():
    window = tk.Tk()
    window.title(" لیست محصولات ")

    product_list = read_from_file("product")

    tree = ttk.Treeview(window, columns=("name", "top_category", "mid_category", "quantity", "id"),
                        show="headings")

    tree.heading("name", text="نام محصول")
    tree.heading("top_category", text="دسته بندی اول")
    tree.heading("mid_category", text="دسته بندی دوم")
    tree.heading("quantity", text="تعداد ")
    tree.heading("id", text="شناسه")

    for product in product_list:
        tree.insert("", "end", values=(
            product["name"], product["top_category"], product["mid_category"], product["quantity"],
            product["id"]))

    tree.pack(expand=True, fill=tk.BOTH)

    window.mainloop()
