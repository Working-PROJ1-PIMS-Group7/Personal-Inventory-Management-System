import json
from tabulate import tabulate
import random

class ItemManager:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, importance, category):
        item_id = str(random.randint(1000, 9999))
        if importance.lower() not in ['low', 'medium', 'high']:
            print("Importance must be 'Low', 'Medium', or 'High'.")
            return
        item = {
            "Item ID": item_id,
            "Name": name,
            "Quantity": quantity,
            "Importance": importance.capitalize(),  
            "Category": category
        }
        self.items.append(item)
        print("Item added successfully.")

    def edit_item(self, item_id, new_item):
        item_index = -1
        for index, item in enumerate(self.items):
            if item["Item ID"] == item_id:
                item_index = index
                break
        if item_index != -1:
            self.items[item_index] = new_item
            print("Item edited successfully.")
        else:
            print("Item not found.")
            
    def remove_item(self, item_id):
        item_index = -1
        for index, item in enumerate(self.items):
            if item["Item ID"] == item_id:
                item_index = index
                break
        if item_index != -1:
            del self.items[item_index]
            print("Item removed successfully.")
        else:
            print("Item not found.")
            
    def view_items(self):
        if self.items:
            headers = ["Item ID", "Name", "Quantity", "Importance", "Category"]
            print("Search by:")
            print("1. Category")
            print("2. Item Name")
            print("3. View All")
            search_choice = input("Enter your choice (1/2/3): ")
            if search_choice == "1":
                existing_categories = set(item["Category"] for item in self.items)
                print("Existing categories:")
                for category in existing_categories:
                    print(category)
                selected_category = input("Enter the category to filter by: ")
                filtered_items = [item for item in self.items if item["Category"] == selected_category]
            elif search_choice == "2":
                search_name = input("Enter the name of the item to search for: ")
                filtered_items = [item for item in self.items if item["Name"] == search_name]
            elif search_choice == "3":
                print("Sort in:")
                print("1. Ascending order")
                print("2. Descending order")
                order_choice = input("Enter your choice (1/2): ")
                if order_choice == "1":
                    filtered_items = sorted(self.items, key=lambda x: x["Name"])
                elif order_choice == "2":
                    filtered_items = sorted(self.items, key=lambda x: x["Name"], reverse=True)
                else:
                    print("Invalid choice. Displaying unsorted items.")
                    filtered_items = self.items
            else:
                print("Invalid choice. Displaying unfiltered items.")
                filtered_items = self.items

            if filtered_items:
                item_data = [[item["Item ID"], item["Name"], item["Quantity"], item["Importance"], item["Category"]] for item in filtered_items]
                print(tabulate(item_data, headers=headers, tablefmt="grid"))
            else:
                print("No items found.")
        else:
            print("No items to display.")

    def save_data(self, filename):
        with open(filename, "w") as file:
            json.dump(self.items, file)

    def load_data(self, filename):
        try:
            with open(filename, "r") as file:
                self.items = json.load(file)
                print("Data loaded successfully.")
        except FileNotFoundError:
            print("No data file found. Starting with an empty list.")
            self.items = []


def main():
    data_filename = "items_data.json"  
    item_manager = ItemManager()
    item_manager.load_data(data_filename)
    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Edit Item")
        print("3. Remove Item")
        print("4. View Items")
        print("5. Save Data")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            importance = input("Enter the importance (Low/Medium/High): ")
            category = input("Enter the category: ")
            item_manager.add_item(name, quantity, importance, category)
        elif choice == "2":
            item_id = input("Enter the Item ID of the item to edit: ")
            new_name = input("Enter the new item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            new_importance = input("Enter the new importance (Low/Medium/High): ")
            new_category = input("Enter the new category: ")
            new_item = {
                "Item ID": item_id,
                "Name": new_name,
                "Quantity": new_quantity,
                "Importance": new_importance.capitalize(),
                "Category": new_category
            }
            item_manager.edit_item(item_id, new_item)
        elif choice == "3":
            item_id = input("Enter the Item ID of the item to remove: ")
            item_manager.remove_item(item_id)
        elif choice == "4":
            item_manager.view_items()
        elif choice == "5":
            item_manager.save_data(data_filename)
            print("Data saved successfully.")
        elif choice == "6":
            print("Saving data before exiting...")
            item_manager.save_data(data_filename)
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
