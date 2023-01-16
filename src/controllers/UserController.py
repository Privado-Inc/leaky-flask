# pseudo code

import sys
import traceback
from flask import render_template, redirect, url_for, request, abort

import json
from src.models.User import User
from flask import jsonify

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

def index():
    return jsonify({"success": "Done"})

def store():
    from app import db
    if request.method == 'POST':
        print(f"{request.get_data()}")
        task_content = json.loads(request.get_data())
        user = User(firstname=task_content["firstname"], address=task_content["address"], age=task_content["age"])

        try:
            db.create_all()
            db.session.add(user)
            db.session.commit()
            return jsonify({"success": f"Successfully created {user}"})
        except Exception as e:
            print(traceback.format_exc())
            return 'There was an issue adding your task'

def show(user_id):
    try:
        if request.method == 'GET':
            print(f"{request.get_data()}")
            user = User.query.filter_by(id=user_id).first()
            if user:
                return jsonify({"success": f"Retried {user.serialize}"})
            return jsonify({"Failure": f"Retrieve operation failed"})
    except Exception as e:
        print(traceback.format_exc())
        return 'There was an issue while getting users'

def update(userId):
    pass

def delete(userId):
    pass

def destroy(userId):
    pass