class Customer:
    def __init__(self, customerID, name, email, phone, address):
        # Initialize the attributes
        self.customerID = customerID
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def display(self):
        # Display the customer's details
        print(f"Customer Details: {self.customerID}, {self.name}, {self.email}, {self.phone}, {self.address}")

    # Getter methods
    def get_customerID(self):
        return self.customerID

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

    # Save method
    def save_to_file(self, file_path):
        try:
            with open(file_path, 'a') as file:
                file.write(f"{self.customerID},{self.name},{self.email},{self.phone},{self.address}\n")
            print("Customer details saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

# Prompt the user for customer details
customerID = input("Enter Customer ID: ")
name = input("Enter Customer Name: ")
email = input("Enter Customer Email: ")
phone = input("Enter Customer Phone: ")
address = input("Enter Customer Address: ")

# Create an instance of the Customer class with user input
customer1 = Customer(customerID, name, email, phone, address)

# Call the display method to print the customer's details
customer1.display()

# Save customer details to a file
customer1.save_to_file('customer_data.txt')
