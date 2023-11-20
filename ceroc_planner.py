import json
from pprint import pprint

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    # Read data from contacts.json
    contacts_data = read_file('contacts.json')
    print("Contacts:")
    pprint(contacts_data)

    events_data = read_file('events.json')
    print("Events")
    pprint(events_data)

if __name__=="__main__":
    main()