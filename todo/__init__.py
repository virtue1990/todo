from flask import Flask

def create_app():
    app = Flask(__name__)
    from view.todo import blueprint
    app.register_blueprint(blueprint)
    return app
