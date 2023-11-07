from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

# Path to the client_secret.json file downloaded from the Cloud Console
CLIENT_SECRET_FILE = './secret/client_secret_1037817236631-hf1af1iubdue73dos0eq1hham77o0ftf.apps.googleusercontent.com.json'

# The OAuth 2.0 scopes to request.
SCOPES = ['https://mail.google.com/']

# This creates a flow object from the client secrets file.
# This flow object is used to manage the OAuth 2.0 Authorization Grant Flow.
flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, ' '.join(SCOPES))

# Create a Storage object to manage the token file.
# The name of the token file is provided when creating the Storage object.
storage = Storage('credentials.dat')

# Try to retrieve credentials from storage.
# If the credentials don't exist or are invalid, run_flow() is called
# to obtain new credentials from the authorization server.
credentials = run_flow(flow, storage)

# The access token is a string that the client can use to authenticate
access_token = credentials.access_token

# print the access token
print(access_token)