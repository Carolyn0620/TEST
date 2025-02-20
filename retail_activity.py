class Customer: #define the class
    def __init__(self, customerID, name, email, phone, address): #initiate the attribute
        self.customerID = customerID
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
   
    def display(self): #display the method
        print(f"Customer 1 Details: {self.customerID}, {self.name}, {self.email}, {self.phone}, {self.address}")
 
customer1= Customer("123","Carolyn", "lauyeejie20@gmail.com", "0223344555", "15 Rathmines Road") #create an instance
 
customer1.display() #calling the display method