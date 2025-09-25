#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")