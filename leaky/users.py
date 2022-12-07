import sqlite3

from flask import Blueprint, jsonify, session, request, render_template
from sentry_sdk import capture_message, capture_exception 
from .utils import query_db

bp = Blueprint("users", __name__)

@bp.route("/user/add", methods=["POST"])
def create_user():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    location = request.form.get("location")
    age = request.form.get("age")
    if first_name is None or location is None:

        return (
            jsonify(
                {
                    "error": "need firstname, last_name at least"
                }
            ),
            400,
        )

    query = (
        "INSERT INTO user (firstname, lastname, location, age) VALUES ('%s', '%s', '%s', %d)"
        % (first_name, last_name, location, int(age))
    )

    try:
        query_db(query, [], False, True)
        capture_message("Account created for: %s %s" % (first_name, last_name ))
        return jsonify({"success": True})
    except sqlite3.Error as err:
        capture_exception(err)
        return jsonify({"error": "could not create user:" + err})

@bp.route("/user/search", methods=["GET"])
def list_user():
    try:
        id = request.args.get('id', None)
        query = "SELECT firstname, lastname, location, age FROM user WHERE id=?;"
        result = query_db(query, (id))
        capture_message("Account created for: %s" % result)
        return render_template(
            "user_details.html", result=result
        )
    except sqlite3.Error as err:
        message = "Error while executing query " + query_param + ": " + err
        return render_template("error.html", message=message)
