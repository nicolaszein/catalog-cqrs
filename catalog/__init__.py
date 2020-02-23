from flask import Flask, jsonify
from catalog.command.configs.database import DATABASE as command_database # noqa

from catalog.exceptions import ValidatorError

from catalog.web.api import app as api_app


class App:
    _app = None

    def start(self):
        if self._app:
            return None

        app = Flask(__name__)
        self._app = app

        self._app.register_blueprint(api_app)

        self.__register_error_handlers(app)
        self.__register_hooks(app)

        return self._app

    def __register_error_handlers(self, app):
        @app.errorhandler(ValidatorError)
        def handle_validator_error(e):
            return jsonify(errors=e.errors), 400

    def __register_hooks(self, app):
        @app.teardown_appcontext
        def shutdown_session(exception=None):
            command_database.session.close()


app = App().start()
