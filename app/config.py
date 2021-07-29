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
    WORKSPACE_ID = '508ECC2A-010B-4563-8638-777767FD89DD'
    
    # Report Id for which Embed token needs to be generated
    # REPORT_ID = '23c26217-87a9-4dbc-870d-4f53e2ae527c'
    REPORT_ID = 'eaf34c6c-f751-45c9-9688-afbe83adddc3'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = 'eb437f8f-d266-48d5-b9bc-76b0ac9a36b2'
    
    #identity information for RLS

    #LOCATION = userlocation()
    ROLE = 'role1'
    ROLE2 = 'role 2'
    USERNAME = 'user1@roconnor.onmicrosoft.com'

    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '5bcf42b7-2f07-495a-a2a4-26babac05729'
    CLIENT_ID_ROLE_1 = 'fe86c018-abe8-4674-b2e2-fda87c0bf712'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = '~C6pU80~H50T1Pib~l4o30C~B92Zi3US6C'
    CLIENT_SECRET_ROLE_1 = '4ASmPUr8b922MiAa-2H28xI_LWCjw-7J.-'

    DATASET = 'fa711706-0814-45fe-ab58-2124573f25cd'
    
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
    

