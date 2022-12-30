from flask import Blueprint, jsonify, request, render_template
from sentry_sdk import capture_exception

from .utils import send_mail

bp = Blueprint("admin", __name__)

@bp.route("/admin/notify", methods=["POST", "GET"])
def notify():
    if request.method == "POST":
        first_name = request.form.get("firstname")
        message = request.form.get("message")
        if first_name is None or message is None:
            return (
                jsonify({"error": "need first_name, message at least"}),
                400,
            )

        try:
            send_mail(message, first_name)
            return jsonify({"success": True})
        except Exception as e:
            capture_exception(e)
            return jsonify({"error": "could not send mail"})
    
    return render_template('notify.html')