from asyncio import events
from flask import render_template, request
from app import app
from models.event import Event
from models.todo_event import add_new_event, delete_event, event_list

@app.route('/')
def home(): 
    return render_template ("index.html", title="Home", events=event_list)

@app.route('/addevent', methods=['POST'])
def add_event():
    event_date = request.form["date"]
    event_name_of_event = request.form["name"]
    event_number_of_guests = request.form["number"]
    event_room_location = request.form["room"]
    event_description = request.form["description"]
    event_recurring = request.form["recurring"]
    new_event = Event(event_date, event_name_of_event, event_number_of_guests, event_room_location, event_description, event_recurring)
    add_new_event(new_event)
    return render_template ("index.html", title="Home", events=event_list)

@app.route('/deleteevent', methods=['POST'])
def remove_event():
    event_to_remove = event_list.index()
    delete_event(event_to_remove)
