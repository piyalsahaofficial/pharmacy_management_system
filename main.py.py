medicines = []
class Medicine:
    def __init__(self,id,name,price,qty,expiry):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty
        self.expiry = expiry
    
def add_medicine():
        id = int(input("Enter a unique ID: "))
        name = input("Enter the medicine name: ")
        price = float(input("Enter the price of the medicine: "))
        qty = int(input("Enter the quantity: "))
        expiry = input("Enter the expiry date: ")
        medicines.append(Medicine(id, name, price, qty, expiry))
        print("Added")
    
def view_medicine():
    if not medicines:
        print("No medicine available")
        return
        
    for medicine in medicines:
        print("Medicine ID: ", medicine.id)
        print("Name: ", medicine.name)
        print("Price: ", medicine.price)
        print("Quantity: ", medicine.qty)
        print("Expiry Date: ", medicine.expiry)

add_medicine()
view_medicine()



