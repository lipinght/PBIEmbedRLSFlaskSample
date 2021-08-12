# Copyright (c) Microsoft Corporation.

from flask import current_app as app, session
from app.models import User



class BaseConfig(object):

    def userlocation():
        users = User.query.all()
        logged_in_user = None
        if session.get("user_id"):
            logged_in_user = User.query.get(session.get("user_id"))
            location = logged_in_user.location
        return location


    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = ''
 
    # Report Id for which Embed token needs to be generated
    REPORT_ID = ''

    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = ''

    # identity information for RLS
    USERNAME = ''

    # Client Id (Application Id) of the AAD app
    CLIENT_ID = ''

    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = ''
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''


#    
 #   SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or 'prc9FWjeLYh_KsPGm0vJcg'
  #  SQLALCHEMY_DATABASE_URI='sqlite:///'+ os.path.join(basedir, 'globomantics.sqlite')
   # SQLALCHEMY_TRACK_MODIFICATIONS=False
    #DEBUG=True
    

