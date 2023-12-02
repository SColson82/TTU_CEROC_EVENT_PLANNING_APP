from classes.Contact import Contact
from classes.Event import Event

"""
This class represents a tuple of 1 Event and 1 Contact object, meaning the Contact is attending the Event.
This is its own class because there will be attributes associated to a contact attending an event ie
whether they need a parking pass, special accommodations, etc. 

For now, the "memo" attribute is a catch-all for these, but in the future, more attributes will be added
"""

class Event_Attendee(object):
    # an Event object and Contact object are passed into the constructor, essentially creating a tuple object
    def __init__(self, e: Event, c: Contact, memo: str = ""):
       self._event = e
       self._contact = c
       self._memo = memo

    # getters
    @property
    def event(self):
        return self._event
    
    @property
    def contact(self):
        return self._contact
    
    @property
    def memo(self):
        return self._memo

    # setters
    @event.setter
    def event(self, e):
        if isinstance(e, Event):
            self._event = e
        else:
            raise ValueError("This event does not exist.")
    
    @contact.setter
    def contact(self, c):
        if isinstance(c, Contact):
            self._contact == c
        else:
            raise ValueError("This contact does not exist.")
    
    @memo.setter
    def memo(self, value):
        self._memo = value
        #pass

    # This function defines what happens when you print the object as text ie print(Event_Attendee)
    # PRINTS IN THE FORM "John Smith attending Data Science League Meeting"
    def __str__(self):
        """
        python has a few ways of streamlining concatenation of strings.
        each time there's a {} in the string, that represents a variable.
        notice at the end of the string, ".format()"
        the variables passed into this function will replace each {} (in order)
        """
        return "{} {}\nattending\n{}".format(self.contact.firstname, self.contact.lastname, self.event.name)