# # services/users/project/__init__.py

# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import sys

# print(app.config, file=sys.stderr)

# db = SQLAlchemy()

# ##Application Factory pattern
# def create_app(script_info=None):
# # instantiate the app
#     app = Flask(__name__)
#     # set config
#     app_settings = os.getenv('APP_SETTINGS')
#     app.config.from_object(app_settings)

#     # set up extensions
#     db.init_app(app)

#     # register blueprints
#     from project.api.users import users_blueprint
#     app.register_blueprint(users_blueprint)
    
#     # shell context for flask cli
#     @app.shell_context_processor
#     def ctx():
#         return {'app': app, 'db': db}
#     return app

import os # new
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # new
import sys
from flask_cors import CORS

db = SQLAlchemy()

##Application Factory pattern
def create_app(script_info=None):
# instantiate the app
    app = Flask(__name__)

    CORS(app)
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    
    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    return app