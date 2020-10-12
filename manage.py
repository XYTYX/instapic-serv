import os
import unittest

from flask import render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app import blueprint

app = create_app()
app.app_context().push()

@app.route('/')
@app.route('/<string:x>')
def index(x = None):
    return app.send_static_file('index.html') 

app.register_blueprint(blueprint)

manager = Manager(app)

migrate = Migrate(app, db, render_as_batch=True, compare_type=True)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()