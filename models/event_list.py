from models.event import *

event0= Event("01.01.10","Party", 10, "home", "a party",True)
event1= Event("02.02.20","Gig",100,"Venue", "a Band", False)
event2= Event("03.03.30","Dentist",1, "Dentists","its gonna hurt", False)

event_list =[event0, event1, event2]
def add_new_event(new_event):
    event_list.append(new_event)

def delete_event(name):
    for event in event_list:
        if event.name == name:
            event_list.remove(event)