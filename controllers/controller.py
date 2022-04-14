from app import app
from models.event import Event
from models.todo_event import event_list

@app.route('/')
def home(): 
    return "To-Do Event"