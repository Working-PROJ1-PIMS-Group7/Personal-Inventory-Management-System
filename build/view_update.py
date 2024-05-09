from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database 
import sqlite3
import customtkinter

class UpdateWindow(Toplevel):
    def __init__(self, master=None, item_data=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.title("Update Item")
        self.geometry("500x450")
        self.config(bg="#F6F6F6")
        self.resizable(False, False)
        
        font2 = ('JosefinSansRoman Regular', 18, 'normal')

        id_label = customtkinter.CTkLabel(self, font=font2, text='Item ID:', text_color='#000000')
        id_label.place(x=37, y=20)

        self.id_entry = customtkinter.CTkEntry(self, font=font2, text_color="#000000", width=150, height=24, border_width=2)
        self.id_entry.place(x=37, y=50)

        qty_label = customtkinter.CTkLabel(self, font=font2, text='Item Qty:', text_color='#000000')
        qty_label.place(x=205, y=20)

        self.qty_entry = customtkinter.CTkEntry(self, font=font2, text_color="#000000", width=130, height=24, border_width=2)
        self.qty_entry.place(x=205, y=50)

        name_label = customtkinter.CTkLabel(self, font=font2, text='Item Name:', text_color='#000000')
        name_label.place(x=37, y=85)

        self.name_entry = customtkinter.CTkEntry(self, font=font2, text_color="#000000", width=300, height=24, border_width=2)
        self.name_entry.place(x=37, y=120)

        categ_label = customtkinter.CTkLabel(self, font=font2, text='Item Category:', text_color='#000000')
        categ_label.place(x=37, y=150)

        self.categ_entry = customtkinter.CTkEntry(self, font=font2, text_color="#000000", width=130, height=24, border_width=2)
        self.categ_entry.place(x=37, y=180)

        impt_label = customtkinter.CTkLabel(self, font=font2, text='Importance:', text_color='#000000')
        impt_label.place(x=200, y=150)

        importance_values = ["Low", "Medium", "High"]
        self.importance_combobox = ttk.Combobox(
            self,
            values=importance_values,
            state="readonly",
        )
        self.importance_combobox.place(
            x=250.0,
            y=225.0,
            width=170.0,
            height=33.0
        )

        update_button = customtkinter.CTkButton(self,
                                                font=font2,
                                                text_color='#000000',
                                                text='Update Item',
                                                hover_color='#ada69e',
                                                fg_color='#c4b8a9',
                                                cursor='hand2',
                                                corner_radius=8,
                                                width=150,
                                                height=42,
                                                command=self.update_item
                                                )
        update_button.place(x=32, y=250)

        close_button = customtkinter.CTkButton(self,
                                               font=font2,
                                               text_color='#000000',
                                               text='Close Window',
                                               hover_color='#ada69e',
                                               fg_color='#c4b8a9',
                                               cursor='hand2',
                                               corner_radius=8,
                                               width=150,
                                               height=42,
                                               command=self.destroy)
        close_button.place(x=190, y=250)


    def update_item(self):
        id_val = self.id_entry.get()

        if not id_val:
            messagebox.showerror('ERROR', 'ENTER ITEM ID')
            return

        conn = sqlite3.connect('Inventory.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Inventory WHERE id=?", (id_val,))
        if not cursor.fetchone():
            messagebox.showerror('ERROR', 'Item with ID does not exist')
            conn.close()
            return
        else:
            name_val = self.name_entry.get()
            qty_val = self.qty_entry.get()
            importance_val = self.importance_combobox.get()
            categ_val = self.categ_entry.get()

            print(f"Updating item with ID: {id_val}, Name: {name_val}, Quantity: {qty_val}, Importance: {importance_val}, Category: {categ_val}")

            if not (name_val and qty_val and importance_val and categ_val):
                messagebox.showerror('ERROR', 'ENTER ALL FIELDS')
                conn.close()
                return

            try:
                qty_val = int(qty_val)

                update_query = """
                UPDATE Inventory
                SET name=?, in_stock=?, importance=?, category=?
                WHERE id=?
                """
                cursor.execute(update_query, (name_val, qty_val, importance_val, categ_val, id_val))

                conn.commit()

                conn.close()

                print("Database update successful")
                messagebox.showinfo('Success!', 'Data has been updated')
                
            except ValueError as e:
                print(f"ValueError: {e}")
                messagebox.showerror('ERROR', 'Quantity must be an integer')
                conn.close()
            
            except Exception as e:
                print(f"An error occurred: {e}")
                messagebox.showerror('ERROR', f'An error occurred: {e}')
