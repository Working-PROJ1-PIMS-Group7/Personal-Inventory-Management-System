import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database 
from tkinter.ttk import Combobox
from view_inven import InventoryWindow 
import random


app = customtkinter.CTk()
app.title('Personal Inventory Management System')
app.geometry('450x500')
app.config(bg = '#F6F6F6')
app.resizable(False,False)


font1 = ('JosefinSansRoman Regular', 25, 'bold')
font2 = ('JosefinSansRoman Regular', 18, 'normal')
font3 = ('JosefinSansRoman Regular', 13, 'bold')
font4 = ('JosefinSansRoman Regular', 26, 'normal')

lab_window = None  # Global variable to hold lab_window object


def populate_entries_with_data(item_data):
    id_entry.delete(0, END)
    id_entry.insert(0, item_data["Item ID"])
    
    name_entry.delete(0, END)
    name_entry.insert(0, item_data["Name"])
    
    qty_entry.delete(0, END)
    qty_entry.insert(0, item_data["Quantity"])
    
    importance_combobox.set(item_data["Importance"])
    
    categ_entry.delete(0, END)
    categ_entry.insert(0, item_data["Category"])


def populate_entries_with_data(item_data):
    id_entry.delete(0, END)
    id_entry.insert(0, item_data["Item ID"])
    
    name_entry.delete(0, END)
    name_entry.insert(0, item_data["Name"])
    
    qty_entry.delete(0, END)
    qty_entry.insert(0, item_data["Quantity"])
    
    importance_combobox.set(item_data["Importance"])
    
    categ_entry.delete(0, END)
    categ_entry.insert(0, item_data["Category"])




def insert():
    id = id_entry.get()
    name = name_entry.get()
    qty = qty_entry.get()
    importance = importance_combobox.get()
    category = categ_entry.get()
    
    if not ( name and qty and importance and category):
        messagebox.showerror('ERROR','ENTER ALL FIELDS')
    elif database.id_exist(id):
        messagebox.showerror('Error', 'ID already exists')
    else:
        if not id:  # Check if id is empty
            id = str(random.randint(1000, 9999))  # Generate random id
        try:
            qty = int(qty)
            database.insert_item(id, name, qty, importance, category)
            messagebox.showinfo('Success!', 'Data has been inserted')
        except ValueError:
            messagebox.showerror('ERROR', 'Quantity must be an integer')


def close_win():
    app.destroy()

def view_invent():

    view_invent_window = InventoryWindow(master=app)
    #app.withdraw()  # Hide the main window
    view_invent_window.mainloop()  # Start the mainloop of the viewinven window
    app.deiconify()  # Show the main window again after viewinven window is closed


title_label = customtkinter.CTkLabel(app, font = font4, text = 'Personal inventory Management\nSystem',text_color='#000000',bg_color='#F6F6F6')
title_label.place(x = 47, y = 14)

frame = customtkinter.CTkFrame(app, bg_color = '#FFF4E3',corner_radius = 10,width = 1000,height = 500)

frame = customtkinter.CTkFrame(app,bg_color = '#FFF4E3',corner_radius = 10,width = 400,height = 400)
frame.place(x=30, y=90) 

id_label = customtkinter.CTkLabel(frame,font = font2,text = 'Item ID:',text_color='#000000')
id_label.place(x=37, y= 20)

id_entry = customtkinter.CTkEntry(frame,font = font2,text_color= "#000000",width=150,height = 24,border_width=2)
id_entry.place(x=37, y = 50)

qty_label = customtkinter.CTkLabel(frame,font = font2,text = 'Item Qty:',text_color='#000000')
qty_label.place(x=205, y= 20)

qty_entry = customtkinter.CTkEntry(frame,font = font2,text_color= "#000000",width=130,height = 24,border_width=2)
qty_entry.place(x=205, y = 50)

name_label = customtkinter.CTkLabel(frame,font = font2,text = 'Item Name:',text_color='#000000')
name_label.place(x=37, y= 85)

name_entry = customtkinter.CTkEntry(frame,font = font2,text_color= "#000000",width=300,height = 24,border_width=2)
name_entry.place(x=37, y = 120)

categ_label = customtkinter.CTkLabel(frame,font = font2,text = 'Item Category:',text_color='#000000')
categ_label.place(x=37, y= 150)

categ_entry = customtkinter.CTkEntry(frame,font = font2,text_color= "#000000",width=130,height = 24,border_width=2)
categ_entry.place(x=37, y = 180)

impt_label = customtkinter.CTkLabel(frame,font = font2,text = 'Importance:',text_color='#000000')


impt_label.place(x=200, y= 150)

importance_values = ["Low", "Medium", "High"]
importance_combobox = Combobox(
    frame,
    values=importance_values,
    state="readonly",
)
importance_combobox.place(
    x=250.0,
    y=225.0,
    width=170.0,
    height=33.0
)


add_button = customtkinter.CTkButton(frame,
                                     font = font2, 
                                     text_color = '#000000',
                                     text = 'Add Item',
                                     hover_color='#ada69e',
                                     fg_color='#c4b8a9',
                                     cursor = 'hand2',
                                     corner_radius=8,
                                     width = 150,
                                     height = 42,
                                     command=insert)
add_button.place(x = 32, y=250)


view_button = customtkinter.CTkButton(frame,
                                     font = font2, 
                                     text_color = '#000000',
                                     text = 'View Inventory',
                                     hover_color='#ada69e',
                                     fg_color='#c4b8a9',
                                     cursor = 'hand2',
                                     corner_radius=8,
                                     width = 150,
                                     height = 42,
                                     command=view_invent)
view_button.place(x = 190, y=250)


close_button = customtkinter.CTkButton(frame,
                                     font = font2, 
                                     text_color = '#000000',
                                     text = 'Close App',
                                     hover_color='#ada69e',
                                     fg_color='#c4b8a9',
                                     cursor = 'hand2',
                                     corner_radius=8,
                                     width = 150,
                                     height = 42,
                                     command = close_win)
close_button.place(x = 109, y=300)

app.mainloop()
