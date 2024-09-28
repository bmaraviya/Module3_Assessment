import os

log_file = "transaction_log.txt"

def log_transaction(message):
    with open(log_file, "a") as log:
        log.write(message + "\n")

def banker_menu(customers):
    while True:
        display_banker_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_customer(customers)
        elif choice == '2':
            view_customer(customers)
        elif choice == '3':
            search_customer(customers)
        elif choice == '4':
            view_all_customers(customers)
        elif choice == '5':
            total_amount(customers)
        else:
            print("Exiting Banker Menu...")
            break

def add_customer(customers):
    name = input("Enter customer name: ")
    balance = float(input("Enter initial balance: "))
    customer_id = len(customers) + 1
    customers[customer_id] = {"name": name, "balance": balance}
    log_transaction(f"Customer {name} added with balance {balance}")
    print(f"Customer {name} added successfully.")

def view_customer(customers):
    customer_id = int(input("Enter customer ID to view: "))
    if customer_id in customers:
        print(f"Customer ID: {customer_id}")
        print(f"Name: {customers[customer_id]['name']}")
        print(f"Balance: {customers[customer_id]['balance']}")
    else:
        print("Customer not found!")

def search_customer(customers):
    name = input("Enter customer name to search: ")
    found = False
    for customer_id, details in customers.items():
        if details['name'].lower() == name.lower():
            print(f"Customer ID: {customer_id}, Name: {details['name']}, Balance: {details['balance']}")
            found = True
    if not found:
        print("Customer not found!")

def view_all_customers(customers):
    if customers:
        print("\n--- All Customers ---")
        for customer_id, details in customers.items():
            print(f"ID: {customer_id}, Name: {details['name']}, Balance: {details['balance']}")
    else:
        print("No customers in the bank.")

def total_amount(customers):
    total = sum(details['balance'] for details in customers.values())
    print(f"Total Amount in the Bank: {total}")
    log_transaction(f"Total amount calculated: {total}")

def customer_menu(customers):
    while True:
        display_customer_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            withdraw_amount(customers)
        elif choice == '2':
            deposit_amount(customers)
        elif choice == '3':
            view_balance(customers)
        else:
            print("Exiting Customer Menu...")
            break

def withdraw_amount(customers):
    customer_id = int(input("Enter customer ID: "))
    if customer_id in customers:
        amount = float(input("Enter amount to withdraw: "))
        if customers[customer_id]['balance'] >= amount:
            customers[customer_id]['balance'] -= amount
            log_transaction(f"Customer {customers[customer_id]['name']} withdrew {amount}")
            print(f"Withdrawal successful. New balance: {customers[customer_id]['balance']}")
        else:
            print("Insufficient balance!")
    else:
        print("Customer not found!")

def deposit_amount(customers):
    customer_id = int(input("Enter customer ID: "))
    if customer_id in customers:
        amount = float(input("Enter amount to deposit: "))
        customers[customer_id]['balance'] += amount
        log_transaction(f"Customer {customers[customer_id]['name']} deposited {amount}")
        print(f"Deposit successful. New balance: {customers[customer_id]['balance']}")
    else:
        print("Customer not found!")

def view_balance(customers):
    customer_id = int(input("Enter customer ID: "))
    if customer_id in customers:
        print(f"Customer ID: {customer_id}, Balance: {customers[customer_id]['balance']}")
    else:
        print("Customer not found!")

def display_main_menu():
    print("\n\tWELCOME TO PYTHON BANK MANAGEMENT SYSTEM\n")
    print("\tSelect your role")
    print("\t1) Banker")
    print("\t2) Customer")
    print("\t3) Exit\n")

def display_banker_menu():
    print("\nWelcome to Banker's App")
    print("\n\tOperations Menu")
    print("\t1) Add Customer")
    print("\t2) View Customer")
    print("\t3) Search Customer")
    print("\t4) View All Customers")
    print("\t5) Total Amounts in Bank")
    print("\t6) Exit\n")

def display_customer_menu():
    print("\nWelcome to Customer's App")
    print("\n\tOperations Menu")
    print("\t1) Withdraw Amount")
    print("\t2) Deposit Amount")
    print("\t3) View Balance")
    print("\t4) Exit\n")

def main():
    customers = {}
    
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            banker_menu(customers)
        elif choice == '2':
            customer_menu(customers)
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid input, please try again.")

main()
