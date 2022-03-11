from flask import Flask, redirect, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from apifairy import APIFairy
from flask_cors import CORS

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
ma = Marshmallow()
cors = CORS()
apifairy = APIFairy()




def create_app(config_class= Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # extensions
    from api import models
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    ma.init_app(app)
    cors.init_app(app)
    apifairy.init_app(app)
    
    
    # blueprints
    from api.errors import errors
    app.register_blueprint(errors)
    
    from api.animals import animals
    app.register_blueprint(animals)
    
    from api.enclosure import enclosure
    app.register_blueprint(enclosure)
    
    # define the shell context
    @app.shell_context_processor
    def shell_context():  # pragma: no cover
        ctx = {'db': db}
        for attr in dir(models):
            model = getattr(models, attr)
            if hasattr(model, '__bases__') and \
                    db.Model in getattr(model, '__bases__'):
                ctx[attr] = model
        return ctx
    
    @app.route('/')
    def index():  # pragma: no cover
        return redirect(url_for('apifairy.docs'))
    
    
    return app