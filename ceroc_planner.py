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

def update_communication_date(contact_objects):
    email_to_lookup = input("Enter the email of the contact you wish to update: ")
    found_contact = None

    for contact in contact_objects:
        if contact.EmailAddress == email_to_lookup:
            found_contact = contact
            break
    if found_contact: 
        last_communication_date = found_contact.LastCommunicationDate
        print(f"Last Date of Communication: {last_communication_date}")

        new_communication_date = input("Enter new last communication date (YYYY-MM-DD): ")
        found_contact.LastCommunicationDate = new_communication_date
        print(f"Updated Last Communication Date: {found_contact.LastCommunicationDate}")
    else:
        print(f"Contact with email {email_to_lookup} not found.")

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
            print("Fix me too.")

        # Exit
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break

        # Error check
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

        
if __name__=="__main__":
    main()