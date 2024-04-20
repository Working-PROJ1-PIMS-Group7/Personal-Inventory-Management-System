import customtkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import database
from Python import Main

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\paule\OneDrive\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x500")
window.configure(bg = "#F6F6F6")


canvas = Canvas(
    window,
    bg = "#F6F6F6",
    height = 500,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
window.resizable(False, False)
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    500.0,
    36.0,
    image=image_image_1
)

canvas.create_text(
    0.0,
    14.0,
    anchor="nw",
    text="PERSONAL INVENTORY MANAGEMENT SYSTEM",
    fill="#5F5135",
    font=("JosefinSansRoman Regular", 26 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
add_item = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("add item clicked"),
    relief="flat"
)
add_item.place(
    x=32.0,
    y=373.0,
    width=171.0,
    height=42.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
view_inventory = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
view_inventory.place(
    x=220.0,
    y=373.0,
    width=174.0,
    height=42.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
edit_item = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
edit_item.place(
    x=32.0,
    y=433.0,
    width=171.0,
    height=42.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
remove_item = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
remove_item.place(
    x=220.0,
    y=432.0,
    width=174.0,
    height=42.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    834.5,
    29.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=686.0,
    y=10.0,
    width=297.0,
    height=36.0
)

canvas.create_text(
    32.0,
    135.0,
    anchor="nw",
    text="ITEM NO.:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    163.0,
    249.0,
    anchor="nw",
    text="IMPORTANCE:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    32.0,
    249.0,
    anchor="nw",
    text="ITEM QTY:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    32.0,
    192.0,
    anchor="nw",
    text="ITEM NAME:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    90.5,
    287.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=32.0,
    y=272.0,
    width=117.0,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    213.5,
    287.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=163.0,
    y=272.0,
    width=101.0,
    height=28.0
)

canvas.create_text(
    292.0,
    249.0,
    anchor="nw",
    text="CATEGORY",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    342.5,
    287.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=292.0,
    y=272.0,
    width=101.0,
    height=28.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    213.0,
    168.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=32.0,
    y=154.0,
    width=362.0,
    height=27.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    213.0,
    225.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=32.0,
    y=211.0,
    width=362.0,
    height=27.0
)

style = ttk.Style(window)

style.theme_use('clam')



window.mainloop()
