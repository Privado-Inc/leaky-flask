from flask import Blueprint

from src.controllers.UserController import index, destroy, store, show, update

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/', methods=['POST'])(store)
user_bp.route('/<int:user_id>', methods=['GET'])(show)
user_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
user_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)
