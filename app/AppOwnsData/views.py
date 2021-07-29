from flask import Blueprint, render_template, session, send_from_directory
import flask
from app.models import User
from app.AppOwnsData.services.xpbiembedservice import PbiEmbedService
from app.AppOwnsData.utils import Utils
import json
import os
from flask import current_app
#import app
pbi = Blueprint('pbi', __name__, template_folder='templates', static_folder='static')




def create_app():
    app = flask(__name__)
    with ap.app_context():
        init_db()
    return app


@pbi.route('/powerbi')

def home():
    users = User.query.all()
    logged_in_user = None
    if session.get("user_id"):
        logged_in_user = User.query.get(session.get("user_id"))
    return render_template('pbi.html', users=users, logged_in_user=logged_in_user)
    #return render_template('pbi.html')

@pbi.route('/powerbi/getembedinfo', methods=['GET'])
def get_embed_info():
    '''Returns report embed configuration'''
    users = User.query.all()
    location = None
    if session.get("user_id"):
        location = User.query.get(session.get("user_id")).location
 
    
    config_result = Utils.check_config(current_app)
    if config_result is not None:
        return json.dumps({'errorMsg': config_result}), 500
    
    try:
        #embed_info = PbiEmbedService().get_embed_params_for_single_report(current_app.config['WORKSPACE_ID'], current_app.config['REPORT_ID'])
        embed_info = PbiEmbedService().RLS(current_app.config['WORKSPACE_ID'], current_app.config['REPORT_ID'], current_app.config['USERNAME'],location)
        return embed_info
    except Exception as ex:
        return json.dumps({'errorMsg': str(ex)}), 500

@pbi.route('/powerbi/favicon.ico', methods=['GET'])
def getfavicon():

    
    
    

    return send_from_directory(os.path.join(pbi.root_path, 'static'), 'img/favicon.ico', mimetype='image/vnd.microsoft.icon')



