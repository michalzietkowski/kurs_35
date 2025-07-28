from flask import Blueprint
from flask.views import MethodView

users_blueprint = Blueprint('users', __name__)


class UsersView(MethodView):
    def get(self):
        return "List of users"

    def post(self):
        return "Add a new user"

    def put(self):
        return "Update an existing user"

    def delete(self):
        return "Delete a user"

users_view = UsersView.as_view('users')
users_blueprint.add_url_rule('/users', view_func=users_view, methods=['GET', 'POST', 'PUT', 'DELETE'])