import tkinter as tk
import sqlite3

def fetch_importance_values():
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT importance FROM Inventory')
    values = [item[0] for item in cursor.fetchall()]
    conn.close()
    return values

def fetch_category_values():
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT category FROM Inventory')
    values = [item[0] for item in cursor.fetchall()]
    conn.close()
    return values

def delete_item(item_id):
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Inventory WHERE item_id = ?', (item_id,))
    conn.commit()
    conn.close()

def display_data():
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Inventory')
    data = cursor.fetchall()
    conn.close()
    
    for row in data:
        print(row)

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

    if search_query and selected_importance != "Select Importance":
            # Filter items based on search query and selected importance
        cursor.execute(f"SELECT * FROM Inventory WHERE lower(Name) LIKE '%{search_query}%' AND Importance = '{selected_importance}' OR lower(Category) LIKE '%{search_query}%' AND Importance = '{selected_importance}'")
    elif selected_importance != "Select Importance":
            # Filter items based on selected importance
            cursor.execute(f"SELECT * FROM Inventory WHERE Importance = '{selected_importance}'")
    elif search_query:
            # Filter items based on search query
        cursor.execute(f"SELECT * FROM Inventory WHERE lower(Name) LIKE '%{search_query}%' OR lower(Category) LIKE '%{search_query}%'")
    else:
        cursor.execute('SELECT * FROM Inventory')
    
    items = cursor.fetchall()
        
        # Close the database connection
    conn.close()

        # Populate Treeview with filtered items
    for item in items:
        self.inventory_tree.insert("", "end", values=item)

def filter_by_importance(inventory_tree, search_var, importance_combobox):
    # Clear existing items
    for item in inventory_tree.get_children():
        inventory_tree.delete(item)

    # Fetch items from database
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    
    # Get the search query from the search entry
    search_query = search_var.get().lower()

    # Get the selected importance value from the combobox
    selected_importance = importance_combobox.get()

    if search_query and selected_importance != "Select Importance":
        # Filter items based on search query and selected importance
        cursor.execute(f"SELECT * FROM Inventory WHERE lower(Name) LIKE '%{search_query}%' AND Importance = '{selected_importance}' OR lower(Category) LIKE '%{search_query}%' AND Importance = '{selected_importance}'")
    elif selected_importance != "Select Importance":
        # Filter items based on selected importance
        cursor.execute(f"SELECT * FROM Inventory WHERE Importance = '{selected_importance}'")
    elif search_query:
        # Filter items based on search query
        cursor.execute(f"SELECT * FROM Inventory WHERE lower(Name) LIKE '%{search_query}%' OR lower(Category) LIKE '%{search_query}%'")
    else:
        cursor.execute('SELECT * FROM Inventory')

    items = cursor.fetchall()
    
    # Close the database connection
    conn.close()

    # Populate Treeview with filtered items
    for item in items:
        inventory_tree.insert("", "end", values=item)

def filter_by_category(inventory_tree, search_var, category_combobox):
    # Clear existing items
    for item in inventory_tree.get_children():
        inventory_tree.delete(item)

    # Fetch items from database
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    
    # Get the search query from the search entry
    search_query = search_var.get().lower()

    # Get the selected category value from the combobox
    selected_category = category_combobox.get()

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
    
    # Close the database connection
    conn.close()

    # Populate Treeview with filtered items
    for item in items:
        inventory_tree.insert("", "end", values=item)
