# init.py

from flask import Flask


def create_app():
    app = Flask(__name__,'/static')
    global api_key
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    # blueprint for auth routes in our app
    from .chat import chat as chat_blueprint
    app.register_blueprint(chat_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for auth routes in our app
    from .upl import upl as upl_blueprint
    app.register_blueprint(upl_blueprint)

    return app