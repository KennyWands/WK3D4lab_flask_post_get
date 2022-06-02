from flask import render_template, request
from app import app
from models.event_list import event_list, add_new_event, delete_event
from models.event import Event


@app.route("/Upcoming")
def index():
    return render_template("index.html", title="Upcoming Events", events=event_list)


@app.route("/Upcoming", methods=["POST"])
def new_event():
    new_date = request.form["date"]
    new_name = request.form["name"]
    new_guests = request.form["guests"]
    new_location = request.form["location"]
    new_description = request.form["description"]
    new_recur = request.form["recurring"]
    new_event = Event(
        new_date, new_name, new_guests, new_location, new_description, new_recur
    )
    add_new_event(new_event)
    return render_template("index.html", title="Upcoming Events", events=event_list)


@app.route("/event/delete", methods=["POST"])
def remove_event():
    event_to_be_deleted = request.form["to_remove"]
    delete_event(event_to_be_deleted)

    return render_template("index.html", title="Upcoming Events", events=event_list)
