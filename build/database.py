import sqlite3

def create_table():
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Inventory(
            id TEXT PRIMARY KEY,
            name TEXT,
            in_stock INTEGER,
            importance TEXT,
            category TEXT)''')
    conn.commit()
    conn.close()

def fetch_items():
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.crsor()
    cursor.execute('SELECT * FROM Items')
    Items = cursor.fetchall()
    conn.close()
    return Items

def insert_item(id, name, in_stock, importance, category):
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Items (id, name, in_stock, impportance, category) VALUES(?, ?, ?, ?, ?)',
                   (id, name, in_stock, importance, category))
    conn.commit()
    conn.close()

def delete_item(id):
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Items WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def update_item(new_name, new_stock, new_importance, new_category, id):
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Items SET name = ?, in_stock = ?, importance = ?, category= WHERE id = ?",
                   (new_name, new_stock, new_importance, new_category, id))
    conn.commit()
    conn.close()

def id_exist(id):
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Items WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

create_table() 