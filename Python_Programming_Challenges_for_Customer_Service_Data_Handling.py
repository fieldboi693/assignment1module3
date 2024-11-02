# Initial sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to generate a new unique ticket ID
def generate_ticket_id():
    ticket_id = "Ticket" + str(len(service_tickets) + 1).zfill(3)
    return ticket_id

# Function to open a new service ticket
def open_new_ticket(customer, issue):
    ticket_id = generate_ticket_id()
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print(f"New ticket opened: {ticket_id}")

# Function to update the status of an existing ticket
def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}")
    else:
        print(f"Ticket {ticket_id} not found.")

# Function to display all tickets or filter by status
def display_tickets(status_filter=None):
    if status_filter:
        filtered_tickets = {k: v for k, v in service_tickets.items() if v["Status"] == status_filter}
        if filtered_tickets:
            for ticket_id, details in filtered_tickets.items():
                print(f"{ticket_id}: {details}")
        else:
            print(f"No tickets found with status '{status_filter}'")
    else:
        for ticket_id, details in service_tickets.items():
            print(f"{ticket_id}: {details}")

# Main menu for interaction
def main():
    while True:
        print("\nCustomer Service Ticket System")
        print("1. Open new ticket")
        print("2. Update ticket status")
        print("3. Display all tickets")
        print("4. Display open tickets")
        print("5. Display closed tickets")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer = input("Enter customer name: ")
            issue = input("Enter issue description: ")
            open_new_ticket(customer, issue)
        
        elif choice == '2':
            ticket_id = input("Enter ticket ID to update: ")
            new_status = input("Enter new status (open/closed): ")
            update_ticket_status(ticket_id, new_status)
        
        elif choice == '3':
            display_tickets()
        
        elif choice == '4':
            display_tickets("open")
        
        elif choice == '5':
            display_tickets("closed")
        
        elif choice == '6':
            print("Exiting system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Start the system
if __name__ == "__main__":
    main()