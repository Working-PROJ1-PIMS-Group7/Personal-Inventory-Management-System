import sqlite3

def create_table():
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Inventory(
            id  TEXT PRIMARY KEY,
            name TEXT,
            in_stock INTEGER,
            importance TEXT,
            category TEXT)''')
    conn.commit()
    conn.close()

def fetch_items():
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Inventory')
    Items = cursor.fetchall()
    conn.close()
    return Items

def insert_item(id, name, in_stock, importance, category):
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Inventory (id, name, in_stock, category, importance) VALUES(?, ?, ?, ?, ?)',
                   (id, name, in_stock, category, importance))
    conn.commit()
    conn.close()

def delete_item(id):
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Inventory WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def update_item(new_name, new_stock, new_category, new_importance, id):
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Inventory SET name = ?, in_stock = ?, category = ?, importance = ? WHERE id = ?",
                   (new_name, new_stock, new_category, new_importance, id))
    conn.commit()
    conn.close()

def id_exist(id):
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Inventory WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

def fetch_items_by_importance(importance):
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Inventory WHERE importance = ?', (importance,))
    items = cursor.fetchall()
    conn.close()
    return items

def fetch_item_by_id(item_id):
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Inventory WHERE id = ?", (item_id,))
    item_data = cursor.fetchone()
    conn.close()
    return item_data

create_table()
