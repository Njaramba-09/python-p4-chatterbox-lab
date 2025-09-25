#!/usr/bin/env python3

from app import app
from models import db, Message

def make_messages():
    Message.query.delete()
    
    messages = [
        Message(body="Hello world!", username="Alice"),
        Message(body="How are you?", username="Bob"),
        Message(body="Great day today!", username="Charlie"),
        Message(body="Working on Flask", username="Duane"),
        Message(body="Learning SQLAlchemy", username="Eve")
    ]

    db.session.add_all(messages)
    db.session.commit()
    print(f"Created {len(messages)} messages")

if __name__ == '__main__':
    with app.app_context():
        make_messages()
