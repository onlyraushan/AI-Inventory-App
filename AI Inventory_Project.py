# AI Inventory App
class Item:
    #create item
    def __init__(self, name, qty, min_qty=5):
        self.name, self.qty, self.min_qty = name, qty, min_qty

class Inventory: #access the manager
    #init system
    def __init__(self):
        self.data = []

    #add item
    def add(self, name, qty, min_qty):
        self.data.append(Item(name, qty, min_qty))

        print(f"Added'{name}' with {qty} units!")

    #view all items
    def view(self):
        if not self.data: return print("Invetory is empty!")

        for i, it in enumerate(self.data, 1):
            alert = "Low" if it.qty <= it.min_qty else ""

            print(f"{i}. {it.name} -  {it.qty} (Min: {it.min_qty}){alert}")

    #AI restock suggestion

    def ai_restock(self):

        low = [i for i in self.data if i.qty <= i.min_qty]

        if low:

            print("\n AI Suggestion: Restock these items:")

            for i in low: print(f"- {i.name} ({i.qty})")

        else:

            print("All item sufficiently stocked!")

    #analytics

    def stats(self):

        if not self.data: return print("No data yet!:")

        most, least = max(self.data, key= lambda x: x.qty), min(self.data, key= lambda x: x.qty)

        total = sum(i.qty for i in self.data)

        print(f"\n Highest Stock: {most.name} ({most.qty})")
        print(f"Lowest Stock: {least.name} ({least.qty})")
        print(f"Total: {total}")

    #sell item

    def sell_item(self, name, qty):

        item = next((i for i in self.fata if i.name.lower() == name.lower()), None)

        if item:

            if qty <= item.qty:
                item.qty -= qty
                print(f"Sold {qty} of '{item.name}'!")

            else:
                print("Not enough stock!")

        else :
            print("Item not found")


class App:

    #start program
    def __init__(self):

        self.inv = Inventory()

    #run menu
    1def run(self):

         while True:

             print("\n AI Inventory")
             print("1 Add Item")
             print("2 View Inventory")
             print("3 AI Restock Suggestion")
             print("4 Analytics")
             print("5 Sell Item")
             print("6 Exit")

             c = input("Choose:")
             if c == "1":
                 n = input("Item name:"); q = int(input("Qty:")); m = int(input("Min Qty Alert: "))
                 self.inv.add(n, q, m)

             elif c == "2": self.inv.view()
             elif c == "3": self.inv.ai_restock()
             elif c == "4": self.inv.stats()
             elif c == "5":
                 n = input("Item name:"); q = int(input("Qty:"))
                 self.inv.sell_item(n, q)
             elif c == "6": print("Thank you!"); break
             else: print("Invalid choice!")

#run

App().run()










