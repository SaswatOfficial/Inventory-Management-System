from core.crud import add_item, view_items, update_item, remove_item
from core.calculate import calculate_average_price, calculate_inventory_value, calculate_highest_quantity_item, calculate_lowest_quantity_item
from prettytable import PrettyTable


def main():
    while True:
        print("\nInventory Management System")
        print("1. Add New Item")
        print("2. View Inventory")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Calculate Total Inventory Value")
        print("6. Calculate Average Item Price")
        print("7. Find Item with Lowest Quantity")
        print("8. Find Item with Highest Quantity")
        print("9. Exit\n\n")
    

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            quantity = input("Enter item quantity: ")
            price = input("Enter item price: ")
            try:
                quantity = int(quantity)
                price = float(price)
                if quantity <= 0 or price <= 0:
                    raise ValueError("Quantity and price must be positive numbers.")
                add_item(name, description, quantity, price)
            except ValueError as e:
                print(f"\n\nError: Please provide valid quantity and price.")

        elif choice == '2':
            print("\nInventory Items:")
            view_items()

        elif choice == '3':
            item_id = input("Enter item ID to update: ")
            name = input("Enter updated name: ")
            description = input("Enter updated description: ")
            quantity = input("Enter updated quantity: ")
            price = input("Enter updated price: ")
            try:
                quantity = int(quantity)
                price = float(price)
                if quantity <= 0 or price <= 0:
                    raise ValueError("Quantity and price must be positive numbers.")
                update_item(item_id, name, description, quantity, price)
            except ValueError as e:
                print(f"\n\nError: Please provide valid quantity and price.")

        elif choice == '4':
            item_id = input("Enter item ID to remove: ")
            remove_item(item_id)

        elif choice == '5':
            total_value = calculate_inventory_value()
            print(f"Total Inventory Value: ${total_value:.2f}")

        elif choice == '6':
            average_price = calculate_average_price()
            print(f"\n\nAverage Item Price: ${average_price:.2f}")

        elif choice == '7':
            lowest_quantity_item = calculate_lowest_quantity_item()
            print("\n\nItem with Lowest Quantity:")
            if lowest_quantity_item:
                table = PrettyTable(["ID", "Name", "Description", "Quantity", "Price"])
                item_id = lowest_quantity_item.get("id", "N/A")
                name = lowest_quantity_item["name"]
                description = lowest_quantity_item["description"]
                quantity = lowest_quantity_item["quantity"]
                price = "${:.2f}".format(lowest_quantity_item["price"])
                table.add_row([item_id, name, description, quantity, price])
                print(table)
            else:
                print("No items in the inventory.")

        elif choice == '8':
            highest_quantity_item = calculate_highest_quantity_item()
            print("\n\nItem with Highest Quantity:")
            if highest_quantity_item:
                table = PrettyTable(["ID", "Name", "Description", "Quantity", "Price"])
                item_id = highest_quantity_item.get("id", "N/A")
                name = highest_quantity_item["name"]
                description = highest_quantity_item["description"]
                quantity = highest_quantity_item["quantity"]
                price = "${:.2f}".format(highest_quantity_item["price"])
                table.add_row([item_id, name, description, quantity, price])
                print(table)
            else:
                print("No items in the inventory.")


        elif choice == '9':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





