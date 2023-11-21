# Import Dependencies
import json
from datetime import datetime
from pprint import pprint

# Contact class
# Input: FirstName, LastName, UID, EmailAddress, Dept, Title,
#           Phone_number, Building, POBox)
class Contact:
    def __init__(self, FirstName: str, LastName: str, UID: int, EmailAddress: str, Dept: str, Title: str, Phone: str, Building: str, POBox: int, LastCommunicationDate=None):
        self.FirstName = FirstName
        self.LastName = LastName
        self.UID = UID
        self.EmailAddress = EmailAddress
        self.Dept = Dept
        self.Title = Title
        self.Phone = Phone
        self.Building = Building
        self.POBox = POBox
        self.LastCommunicationDate = LastCommunicationDate

# Event class
# Input: Name, UID, Date, StartTime, Location, Duration
class Event:
    def __init__(self, Name: str, UID: int, Date: str, StartTime: str, Location: str, Duration: int):
        self.Name = Name
        self.UID = UID
        self.Date = Date
        self.StartTime = StartTime
        self.Location = Location
        self.Duration = Duration
        self.ActionItems = []

    def add_action_item(self, item_name: str, due_date: datetime):
        self.ActionItems.append({"Name": item_name, "Due Date": due_date})

# Function read_file
# Input: path to a json file
# Output: data from the json file
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function create_objects
# Inputs: specified json data, and a class
# Outputs: an object of the specified class using the specified json data
def create_objects(json_data, object_class):
    # Array to hold data
    objects = []
    # Iterate over the provUIDed data
    for item in json_data:
        # Use dictionary unpacking to parse data
        obj = object_class(**item)
        # Save each data item to the array
        objects.append(obj)
    return objects

# Function view_objects
# Input: objects array from the create_objects function and string for header
# Output: the objects created from the json file
def view_objects(objects, object_type):
    print(f"{object_type}s:")
    for object in objects:
        pprint(vars(object))

# Function update_communication_date
# Input: contact objects array
# Output: Updated object with last date of communication noted
def update_communication_date(contact_objects):
    # Prompt user for UID or email
    print("\nEnter the UID or email that you wish to look up: ")
    # Remove leading or trailing whitespace from user input and store
    search_item = input().strip()

    found_contact = None
    # Iterate through contact objects to find the specified contact
    for contact in contact_objects:
        # Remove case sensitivity and check if current obj is the search obj
        if (contact.EmailAddress.lower() == search_item.lower()
            or str(contact.UID) == search_item):
            found_contact = contact
            break
    # If contact is found
    if found_contact: 
        # Display current last date of communication: defaults to none
        last_communication_date = found_contact.LastCommunicationDate
        print(f"Last Date of Communication: {last_communication_date}")

        # Prompt user to update last date of communication
        new_communication_date = input("Enter new last communication date (YYYY-MM-DD): ")
        # Convert string input to datetime and update the contact object
        new_communication_date = datetime.strptime(new_communication_date, '%Y-%m-%d').date().strftime('%Y-%m-%d')
        found_contact.LastCommunicationDate = new_communication_date
        
        # Notify user the object has been updated
        print(f"\nUpdated Last Communication Date: {found_contact.LastCommunicationDate}")
    else:
        # Notify user the object could not be found
        print(f"Contact with search parameter {search_item} not found.")

# Function action_items
# Input: event objects array
# Output: updated event objects with the user's action item and date input
def action_items(events_objects):
    # Prompt user for search parameters
    print("\nEnter the UID, date, or name of the event: ")
    # Remove leading and trailing white space
    search_item = input().strip()

    selected_event = None
    # Iterate over the events object array
    for event in events_objects:
        # Check the current object against the search parameters
        if (
            str(event.UID) == search_item
            or event.Date == search_item
            or event.Name.lower() == search_item.lower()
        ):
            selected_event = event
            break
    # If the event is found
    if selected_event:
        # Display the name of the selected event
        print(f"\nSelected Event: {selected_event.Name}")

        # Loop to add action items to the chosen event
        while True:
            # Collect user input for the name of a single action item, remove leading or trailing whitespace
            item_name = input("\nEnter the action item (or type 'done' to finish): ").strip()
            # Check for the exit condition
            if item_name.lower() == 'done':
                break

            # Collect input for due date
            due_date_str =  input("\nEnter the due date (YYYY-MM-DD): ").strip()
            try: 
                # Convert string input to datetime object
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
                # Add action item and due date to the event object
                selected_event.add_action_item(item_name, due_date.strftime('%Y-%m-%d'))
                # Confirm to user that this has been done
                print(f"\n\nAction item, {item_name}, added with a due date of {due_date}.")
            except ValueError:
                # Error check for correct format
                print("Invalid date format. Please use YYYY-MM-DD.")

            # Print the list of action items added
            print(f"\nAction items associated with {selected_event.Name} on {selected_event.Date}: \n")
            for item in selected_event.ActionItems:
                print(f"Item: {item['Name']}, Due Date: {item['Due Date']}")

    # Notify user that the requested event has not been found
    else: 
        print("Event not found.")

def main():
    # Read data from contacts.json using the read_file function
    contacts_data = read_file('contacts.json')

    # Call the create_objects function on the contacts data
    # and create a Contact object for each contact.
    contact_objects = create_objects(contacts_data, Contact)

    # Read data from the events.json using the read_file function
    events_data = read_file('events.json')
    # Call the create_objects function on the events data 
    events_objects = create_objects(events_data['university_events'], Event)

    # While statement to loop over menu until user is finished.
    while True:

        # Print menu for user
        menu = """\nMenu:
1. View Contacts
2. View Events
3. Input last date of communication for a contact.
4. Add action items to an event.
5. Exit

"""
        print(menu)

        # Take in user's choice
        choice = input("Enter your choice (1-5): ")

        # Converts to integer
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number 1-5.")
            continue
        
        # Print contact list
        if choice == 1:
            view_objects(contact_objects, "Contact")

        # Print event list
        elif choice == 2:
            view_objects(events_objects, "Event")

        # Update date of last contact
        elif choice == 3:
            update_communication_date(contact_objects)

        # Add action items
        elif choice == 4:
            action_items(events_objects)

        # Exit
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break

        # Error check
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

        
if __name__=="__main__":
    main()