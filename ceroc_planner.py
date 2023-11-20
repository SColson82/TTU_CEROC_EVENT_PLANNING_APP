# Import Dependencies
import json
from pprint import pprint

# Contact class
# Input: FirstName, LastName, UID, EmailAddress, Dept, Title,
#           Phone_number, Building, POBox)
class Contact:
    def __init__(self, FirstName: str, LastName: str, UID: int, EmailAddress: str, Dept: str, Title: str, Phone: str, Building: str, POBox: int):
        self.FirstName = FirstName
        self.LastName = LastName
        self.UID = UID
        self.EmailAddress = EmailAddress
        self.Dept = Dept
        self.Title = Title
        self.Phone = Phone
        self.Building = Building
        self.POBox = POBox

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

def view_objects(objects, object_type):
    print(f"{object_type}s:")
    for object in objects:
        pprint(vars(object))



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

    while True:
        menu = """\nMenu:
1. View Contacts
2. View Events
3. Input last date of communication for a contact.
4. Add action items to an event.
5. Exit

"""
        print(menu)
        
        choice = input("Enter your choice (1-5): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number 1-5.")
            continue
        
        if choice == 1:
            view_objects(contact_objects, "Contact")
        elif choice == 2:
            view_objects(events_objects, "Event")
        elif choice == 3:
            print("Fix me.")
        elif choice == 4:
            print("Fix me too.")
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

        
if __name__=="__main__":
    main()