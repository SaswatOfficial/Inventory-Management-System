from core.db import collection

def calculate_inventory_value():
    total_value = 0
    items = collection.find()
    for item in items:
        total_value += item["quantity"] * item["price"]
    return total_value

def calculate_average_price():
    total_price = 0
    total_items = 0
    items = collection.find()
    for item in items:
        total_price += item["price"]
        total_items += 1
    if total_items > 0:
        return total_price / total_items
    else:
        return 0

def calculate_lowest_quantity_item():
    lowest_quantity_item = collection.find_one(sort=[("quantity", 1)])
    return lowest_quantity_item

def calculate_highest_quantity_item():
    highest_quantity_item = collection.find_one(sort=[("quantity", -1)])
    return highest_quantity_item
