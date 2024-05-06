from tkinter import *
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from tkinter import Toplevel, Entry, Button, StringVar, Label, Tk
from tkinter.ttk import Combobox, Treeview
import sqlite3
import database
import utils
from utils import *
from view_update import UpdateWindow

class InventoryWindow(Toplevel):

    

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.font3 = ('JosefinSansRoman Regular', 13, 'bold')
        self.resizable(False,False)


        self.geometry("800x625")
        self.configure(bg="#F6F6F6")
        self.title("VIEW INVENTORY")

        # Protocol to handle window close event
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Category Dropdown Menu
        self.category_var = StringVar()
        self.category_combobox = Combobox(
            self,
            textvariable=self.category_var,
            values = ["Select Category", *self.fetch_category_values()],
            state="readonly",
            font=("Manjari Regular", 15)
        )
        self.category_combobox.place(x=555, y=445, width=225, height=43)
        self.category_combobox.set("Select Category")

        self.delete_button = Button(
            self,
            text="Delete",
            background='#c4b8a9',
            font =("Manjari Regular", 15),
            borderwidth=0,
            highlightthickness=0,
           #corner_radius = 8,
            command=self.delete_item,
            relief="flat",
        )
        self.delete_button.place(x=19, y=445, width=225, height=43)

        self.search_button = Button(
            self,
            text="Search",
            background='#c4b8a9',
            font=("Manjari Regular", 15),
            borderwidth=0,
            highlightthickness=0,
            command=self.populate_treeview,
            relief="flat",
        )
        self.search_button.place(x=350, y=21, width=100, height=30)

        self.search_var = StringVar()
        self.search_entry = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.search_var,
            font=("Arial", 12)
        )
        self.search_entry.place(x=461, y=21, width=300, height=30)

        self.importance_combobox = Combobox(
            self,
            values=["Select Importance","Low","Medium","High"],
            state="readonly",
            font=("Manjari Regular", 15)
        )
        self.importance_combobox.place(
            x=287,
            y=445,
            width=225,
            height=43
        )
        self.importance_combobox.set("Select Importance")
        
        self.imptfilter_button = Button(
            self,
            text="Importance Filter",
            background='#c4b8a9',
            font=("Manjari Regular", 15),
            borderwidth=0,
            highlightthickness=0,
            command=self.filter_by_importance,
            relief="flat",
        )
        self.imptfilter_button.place(x=287, y=495, width=225, height=43)
        
        self.filter_category_button = Button(
            self,
            text="Filter by Category",
            background='#c4b8a9',
            font=("Manjari Regular", 15),
            borderwidth=0,
            highlightthickness=0,
            command=self.filter_by_category,
            relief="flat",
        )
        self.filter_category_button.place(x=555, y=495, width=225, height=43)
        

        self.update_button = Button(
            self,
            text="Update Item",
            background='#c4b8a9',
            font=("Manjari Regular", 12),
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command = self.open_update_window,
        )
        self.update_button.place(x=19, y=495, width=110, height=43)
        

        self.update_table_button = Button(
            self,
            text="Update Table",
            background="#c4b8a9",
            font=("Manjari Regular", 12),
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=self.update_treeview
        )
        self.update_table_button.place(x = 131.5,y = 495, width = 110, height = 43)

        # Adding the label "VIEWING ALL INVENTORY"

        self.label = Label(
            self,
            text="VIEWING ALL INVENTORY",
            bg="#F6F6F6",
            fg="#000000",
            font=("Manjari Regular", 15)
        )
        self.label.place(x=16, y=21)

        
        # Create Treeview widget for displaying inventory
        

        self.inventory_tree = Treeview(
            self,
            columns=("Item ID", "Name", "Quantity", "Importance", "Category"),
            show="headings",
            height=15
        )
        
        # Set column headings
        self.inventory_tree.heading("Item ID", text="Item ID")
        self.inventory_tree.heading("Name", text="Name")
        self.inventory_tree.heading("Quantity", text="Quantity")
        self.inventory_tree.heading("Importance", text="Importance")
        self.inventory_tree.heading("Category", text="Category")

        # Set column widths
        self.inventory_tree.column("Item ID", width=100)
        self.inventory_tree.column("Name", width=220)
        self.inventory_tree.column("Quantity", width=80)
        self.inventory_tree.column("Importance", width=150)
        self.inventory_tree.column("Category", width=200)

        self.inventory_tree.place(x=20, y=70)
        # Populate Treeview with data from database
        self.populate_treeview()



    def open_update_window(self):
        # Fetch the first item from the tree
        first_item = self.inventory_tree.get_children()[0]

        if not first_item:
            messagebox.showerror("Error", "No items available to update.")
            return

        item_id = self.inventory_tree.item(first_item, "values")[0]

        # Fetch item data from database based on item_id
        item_data = database.fetch_item_by_id(item_id)  # Assuming you have a function to fetch item data by ID

        # Create an instance of UpdateWindow with self as the master
        update_window = UpdateWindow(item_data=item_data)
        update_window.mainloop()  # Run the mainloop of the UpdateWindow


    def fetch_importance_values(self):
        conn = sqlite3.connect('Inventory.db')
        cursor = conn.cursor()
        cursor.execute('SELECT importance FROM Inventory')
        values = [item[0] for item in cursor.fetchall()]
        conn.close()
        return values

    def fetch_category_values(self):
        conn = sqlite3.connect('Inventory.db')
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT category FROM Inventory')
        values = [item[0] for item in cursor.fetchall()]
        conn.close()
        return values

    def on_close(self):
        self.master.deiconify()  # Show the main window again
        self.destroy()  # Close the InventoryWindow


    #def sort_by_importance()
    
    def delete_item(self):
        # Get the selected items from the treeview
        selected_items = self.inventory_tree.selection()
        
        if not selected_items:
            messagebox.showerror("Error", "Please select one or more items to delete.")
            return
    
        # Confirm deletion
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected items?")
        if not confirm:
            return
    
        # Iterate over selected items and delete them
        for item in selected_items:
            # Get the item ID from the selected item
            item_id = self.inventory_tree.item(item, "values")[0]
            
            # Delete item from the database
            database.delete_item(item_id)
    
            # Delete item from the treeview
            self.inventory_tree.delete(item)

    def display_data(self):
        utils.display_data()
    
    #updating the tree view button click
    def update_treeview(self):
        # Clear existing items
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)

        # Fetch items from database
        conn = sqlite3.connect('Inventory.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Inventory')
        items = cursor.fetchall()
        conn.close()

        # Populate Treeview with fetched items
        for item in items:
            self.inventory_tree.insert("", "end", values=item)
            self.update_category_combobox()



    def populate_treeview(self):
        # Clear existing items
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)

        # Fetch items from database
        conn = sqlite3.connect('Inventory.db')
        cursor = conn.cursor()
        
        # Get the search query from the search entry
        search_query = self.search_var.get().lower()
        
        if search_query:
            # Filter items based on search query
            cursor.execute(f"SELECT * FROM Inventory WHERE lower(Name) LIKE '%{search_query}%' OR lower(Category) LIKE '%{search_query}%'")
        else:
            cursor.execute('SELECT * FROM Inventory')
        
        items = cursor.fetchall()
        conn.close()

        # Populate Treeview with filtered items
        for item in items:
            self.inventory_tree.insert("", "end", values=item)
    

    def filter_by_importance(self):
        # Clear existing items
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)

        # Fetch items from database
        conn = sqlite3.connect('Inventory.db')
        cursor = conn.cursor()
        
        # Get the search query from the search entry
        search_query = self.search_var.get().lower()

        # Get the selected importance value from the combobox
        selected_importance = self.importance_combobox.get()

        # Base SQL query
        sql_query = 'SELECT * FROM Inventory'

        # Conditions list
        conditions = []

        if search_query:
            conditions.append(f"(lower(Name) LIKE '%{search_query}%' OR lower(Category) LIKE '%{search_query}%')")

        if selected_importance != "Select Importance":
            conditions.append(f"Importance = '{selected_importance}'")

        # If no conditions are added, sort by importance from Low to High
        if not conditions:
            sql_query += ' ORDER BY CASE WHEN Importance = "Low" THEN 1 WHEN Importance = "Medium" THEN 2 WHEN Importance = "High" THEN 3 ELSE 4 END'
        else:
            # Combine conditions with 'AND'
            sql_query += ' WHERE ' + ' AND '.join(conditions)

        cursor.execute(sql_query)
        items = cursor.fetchall()
        
        # Close the database connection
        conn.close()

        # Populate Treeview with filtered/sorted items
        for item in items:
            self.inventory_tree.insert("", "end", values=item)






    def filter_by_category(self):
        # Clear existing items
        self.filter_active = True
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)

        # Fetch items from database
        conn = sqlite3.connect('Inventory.db')
        cursor = conn.cursor()
        
        # Get the search query from the search entry
        search_query = self.search_var.get().lower()

        # Get the selected category value from the combobox
        selected_category = self.category_combobox.get()

        if search_query and selected_category != "Select Category":
            # Filter items based on search query and selected category
            cursor.execute(f"SELECT * FROM Inventory WHERE lower(Name) LIKE '%{search_query}%' AND Category = '{selected_category}' OR lower(Category) LIKE '%{search_query}%' AND Category = '{selected_category}'")
        elif selected_category != "Select Category":
            # Filter items based on selected category
            cursor.execute(f"SELECT * FROM Inventory WHERE Category = '{selected_category}'")
        elif search_query:
            # Filter items based on search query
            cursor.execute(f"SELECT * FROM Inventory WHERE lower(Name) LIKE '%{search_query}%' OR lower(Category) LIKE '%{search_query}%'")
        else:
            cursor.execute('SELECT * FROM Inventory')
    
        items = cursor.fetchall()
        self.filter_active = False
        # Close the database connection
        conn.close()

        # Populate Treeview with filtered items
        for item in items:
            self.inventory_tree.insert("", "end", values=item)

    def update_category_combobox(self):
        # Fetch updated category values from database
        category_values = self.fetch_category_values()
    
        # Update category combobox
        self.category_combobox['values'] = ["Select Category", *category_values]
        self.category_combobox.set("Select Category")
