class SupermarketElectronics:
    def __init__(self):
        self.inventory = {}
        self.sales = []

    def add_item(self, item_id, name, quantity, price):
        self.inventory[item_id] = {'name': name, 'quantity': quantity, 'price': price}
        print(f"Item {name} added to inventory.")

    def update_item(self, item_id, name=None, quantity=None, price=None):
        if item_id in self.inventory:
            if name:
                self.inventory[item_id]['name'] = name
            if quantity:
                self.inventory[item_id]['quantity'] = quantity
            if price:
                self.inventory[item_id]['price'] = price
            print(f"Item {item_id} updated.")
        else:
            print("Item not found in inventory.")

    def remove_item(self, item_id):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f"Item {item_id} removed from inventory.")
        else:
            print("Item not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for item_id, details in self.inventory.items():
            print(f"ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}")

    def record_sale(self, item_id, quantity):
        if item_id in self.inventory:
            if self.inventory[item_id]['quantity'] >= quantity:
                self.inventory[item_id]['quantity'] -= quantity
                sale_record = {
                    'item_id': item_id,
                    'name': self.inventory[item_id]['name'],
                    'quantity': quantity,
                    'price': self.inventory[item_id]['price'],
                    'total': quantity * self.inventory[item_id]['price']
                }
                self.sales.append(sale_record)
                print(f"Sale recorded: {sale_record}")
            else:
                print("Not enough stock to complete the sale.")
        else:
            print("Item not found in inventory.")

    def display_sales_history(self):
        print("Sales History:")
        for sale in self.sales:
            print(sale)

    def generate_sales_report(self):
        total_revenue = sum(sale['total'] for sale in self.sales)
        total_items_sold = sum(sale['quantity'] for sale in self.sales)
        print(f"Total Revenue: ${total_revenue}")
        print(f"Total Items Sold: {total_items_sold}")

def main():
    store = SupermarketElectronics()
    while True:
        print("\nSupermarket Electronics Management System")
        print("1. Add Item to Inventory")
        print("2. Update Item in Inventory")
        print("3. Remove Item from Inventory")
        print("4. Display Inventory")
        print("5. Record a Sale")
        print("6. Display Sales History")
        print("7. Generate Sales Report")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item_id = input("Enter item ID: ")
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            store.add_item(item_id, name, quantity, price)
        elif choice == '2':
            item_id = input("Enter item ID: ")
            name = input("Enter new name (or leave blank): ")
            quantity = input("Enter new quantity (or leave blank): ")
            price = input("Enter new price (or leave blank): ")
            store.update_item(item_id, name or None, int(quantity) if quantity else None, float(price) if price else None)
        elif choice == '3':
            item_id = input("Enter item ID to remove: ")
            store.remove_item(item_id)
        elif choice == '4':
            store.display_inventory()
        elif choice == '5':
            item_id = input("Enter item ID for sale: ")
            quantity = int(input("Enter quantity: "))
            store.record_sale(item_id, quantity)
        elif choice == '6':
            store.display_sales_history()
        elif choice == '7':
            store.generate_sales_report()
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
