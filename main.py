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

def save_data():
     with open("medicines.txt", "w") as file:
          for med in medicines:
               file.write(
                    str(med.id) + "," + 
                    med.name + "," + 
                    str(med.price) + "," + 
                    str(med.qty) + "," +
                    med.expiry + "\n"
               )
     print("Data Saved Successfully!")

def load_data():
     try:
          medicines.clear()

          with open("medicines.txt", "r") as file:
               for line in file:
                    data = line.strip().split(",")

                    med_id = int(data[0])
                    name = data[1]
                    price = float(data[2])
                    qty = int(data[3])
                    expiry = data[4]

                    medicines.append(
                         Medicine(med_id, name, price, qty, expiry)
                    )
          print("Data loaded successfully")
     except FileNotFoundError:
          print("No saved data found")          



while True:
     print("\n    SMART PHARMACY    ")
     print("1. Add Medicine")
     print("2. View Medicines")
     print("3. Search Medicine")
     print("4. Update Price")
     print("5. Delete Medicine")
     print("6. Save Data")
     print("7. Load Data")
     print("8. Exit")
     choice = input("Enter your choice? ")

     if choice == "1":
          add_medicine()
     elif choice == "2":
          view_medicine()
     elif choice == "3":
          search_medicine()
     elif choice == "4":
          update_price()
     elif choice == "5":
          delete_medicine()
     elif choice == "6":
          save_data()
     elif choice == "7":
          load_data()
     elif choice == "8":
          print("Exiting!")
          break
     else:
          print("Invalid Choice")
