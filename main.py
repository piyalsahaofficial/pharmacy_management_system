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

def search_medicine():
     med_id = int(input("Enter the medicine ID you want? "))
     for med in medicines:
          if med.id == med_id:
               print("Found!")
               print("Medicine Name: ",med.name)
               print("Medicine Price: ",med.price)
               return
     print("Not Found")

def update_price():
     med_name = input("Enter the medicine name: ")
     med_price = float(input("Enter the updated price: "))
     
     for med in medicines:
          if med.name == med_name:
               med.price = med_price
               print("Updated")
               return
     print("Medicine not found!") 

def delete_medicine():
     med_name = input("Which medicine you want to remove? ")
     for med in medicines:
          if med.name == med_name:
               medicines.remove(med)
               print("Deleted")
               return
          
     print("Not found")


add_medicine()
view_medicine()

search_medicine()

update_price()
view_medicine()

delete_medicine()
view_medicine()
