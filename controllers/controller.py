from asyncio import events
from flask import render_template
from app import app
from models.event import Event
from models.todo_event import event_list

@app.route('/')
def home(): 
    return render_template ("index.html", title="Home", events=event_list)