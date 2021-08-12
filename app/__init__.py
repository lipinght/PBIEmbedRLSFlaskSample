import os
from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import json
#from AppOwnsData.services.pbiembedservice import PbiEmbedService
#from AppOwnsData.utils import Utils


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config.from_mapping(
    SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or 'prc9FWjeLYh_KsPGm0vJcg',
    SQLALCHEMY_DATABASE_URI='sqlite:///'+ os.path.join(basedir, 'globomantics.sqlite'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    DEBUG=True
    )

    app.config.from_object('app.config.BaseConfig')

   # app.config.from_object('app.xconfig.BaseConfig')

    
    db.init_app(app)

    from app.auth.views import auth
    from app.main.views import main
    from app.AppOwnsData.views import pbi
    from app.AppOwnsData.services.xpbiembedservice import PbiEmbedService
    from app.AppOwnsData.utils import Utils

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(pbi)
    


    from app.main.errors import page_not_found
    app.register_error_handler(404, page_not_found)
    
    
    return app
