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
        # print(f"Attempting to create object from data: {item}")
        try:
            # Use dictionary unpacking to parse data
            obj = object_class(**item)
            # Save each data item to the array
            objects.append(obj)
        except Exception as e:
            print(f"Error creating object from data: {item}")
            print(f"Error details: {e}")
    return objects

def main():
    # Read data from contacts.json using the read_file function
    contacts_data = read_file('contacts.json')
    # print("Contacts Data from JSON:")
    # pprint(contacts_data)
    # Call the create_objects function on the contacts data
    # and create a Contact object for each contact.
    contact_objects = create_objects(contacts_data, Contact)
    # print("Contacts Objects:")
    # pprint(contact_objects)
    
    # Print contacts data in a more readable format
    if contact_objects is not None:
        print("\n\nContacts:")
        for item in contact_objects:
            pprint(vars(item))
    else:
        print("Error: contact_objects is None.")

    # Read data from the events.json using the read_file function
    events_data = read_file('events.json')
    # Call the create_objects function on the events data 
    events_objects = create_objects(events_data['university_events'], Event)

    # Print events data in a more readable format
    if events_objects is not None:
        print("\n\nEvents:")
        for item in events_objects:
            pprint(vars(item))
    else:
        print("Error: events_objects is None.")

if __name__=="__main__":
    main()