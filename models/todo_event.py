from models.event import Event

event_1 = Event("14 April", "CodeClan meetup", 10, "CodeClan Edinburgh", "General meeting", "True")
event_2 = Event("28 April", "Anna's birthday", 5, "Anna's house",
"Anna's birthday party", "False")

event_list = [event_1, event_2]

def add_new_event(new_event):
    event_list.append(new_event)

def delete_event(old_event):
    event_list.remove(old_event)