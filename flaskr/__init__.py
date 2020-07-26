import os
from flask import Flask

def create_app(test_config=None): # factory(工場)的function
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True) # appにconfiguration filesはrelative to the instance folderと伝える。
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)
    # * Define and Access the Database
    # Import and call this function from the factory.
    # Place the new code at the end of the factory function before returning the app.

    from . import auth
    app.register_blueprint(auth.bp)
    # * Blueprints and views
    # Import and register the blueprint from the factory using app.register_blueprint().
    # Place the new code at the end of the factory function before returning the app.

    return app