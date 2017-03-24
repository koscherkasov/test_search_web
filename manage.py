from flask import current_app
from flask_script import Manager
from test_search_app.app import app

manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=current_app)


if __name__ == '__main__':
    manager.run()
