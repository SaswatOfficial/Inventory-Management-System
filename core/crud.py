from itertools import count
from prettytable import PrettyTable
from core.db import collection

id_generator = count(start=1)

def add_item(name, description, quantity, price):
    try:
        quantity = int(quantity)
        price = float(price)
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be positive numbers.")
        
        item_id = next(id_generator)  
        item = {
            "id": item_id,
            "name": name,
            "description": description,
            "quantity": quantity,
            "price": price
        }
        collection.insert_one(item)
        print("\n\nItem added successfully!")
    except ValueError as e:
        print(f"\n\nError: {e}. Please provide valid quantity and price.")
    except Exception as e:
        print(f"\n\nError: {e}. Failed to add the item.")


def update_item(item_id, name, description, quantity, price):
    try:
        item_id = int(item_id)
        quantity = int(quantity)
        price = float(price)
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be positive numbers.")
        
        if not isinstance(quantity, int) or not isinstance(price, float):
            raise ValueError("Invalid quantity or price format.")
        
        query = {"id": item_id}
        new_values = {
            "$set": {
                "name": name,
                "description": description,
                "quantity": quantity,
                "price": price
            }
        }
        result = collection.update_one(query, new_values)
        if result.matched_count > 0 and result.modified_count > 0:
            print("\n\nItem updated successfully!")
        else:
            print("\n\nItem with the specified ID does not exist in the database.")
    except ValueError as e:
        print(f"\n\nError: {e}. Please provide valid item ID, quantity, and price.")
    except Exception as e:
        print(f"\n\nError: {e}. Failed to update the item.")


def remove_item(item_id):
    try:
        item_id = int(item_id)
        item_to_remove = collection.find_one({"id": item_id})
        if item_to_remove:
            collection.delete_one({"id": item_id})
            print("\n\nItem removed successfully!")
        else:
            print("\n\nItem with the specified ID does not exist in the database.")
    except ValueError as e:
        print(f"\n\nError: {e}. Please provide a valid integer ID.")
    except Exception as e:
        print(f"\n\nError: {e}. Failed to remove the item.")


def view_items():
    items = collection.find()
    table = PrettyTable(["ID", "Name", "Description", "Quantity", "Price"])
    for item in items:
        item_id = item.get("id", "N/A")
        name = item["name"]
        description = item["description"]
        quantity = item["quantity"]
        price = item["price"]
        table.add_row([item_id, name, description, quantity, "${:.2f}".format(price)])
    print(table)
