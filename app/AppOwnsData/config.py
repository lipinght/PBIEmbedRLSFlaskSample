# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '508ECC2A-010B-4563-8638-777767FD89DD'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = 'eaf34c6c-f751-45c9-9688-afbe83adddc3'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = 'eb437f8f-d266-48d5-b9bc-76b0ac9a36b2'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '5bcf42b7-2f07-495a-a2a4-26babac05729'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = '~C6pU80~H50T1Pib~l4o30C~B92Zi3US6C'
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''
