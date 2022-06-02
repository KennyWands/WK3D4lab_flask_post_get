class Event():
    def __init__(self,get_date, get_name, get_guests, get_location, get_description,get_recur):
        self.date = get_date
        self.name = get_name
        self.guests = get_guests
        self.location = get_location
        self.description = get_description
        self.recurring = get_recur
        
