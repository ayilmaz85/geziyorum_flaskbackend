from flask import Blueprint, jsonify
from geziyorum.models import User


apiUsers = Blueprint("apiUser", __name__, url_prefix="/api/users")


@apiUsers.route("/")
def users():
    return jsonify("basarili")
