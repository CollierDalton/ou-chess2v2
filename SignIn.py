from flask import Flask, request
from google.oauth2 import id_token
from google.auth.transport import requests

# Specify the CLIENT_ID of the app that accesses the backend:
CLIENT_ID = '1035421752277-7vme3emqji5423fv1s09b64nvam2pfi3.apps.googleusercontent.com'

app = Flask(__name__)

@app.route('/')
def verify_token():
    # token = request.form['https://oauth2.googleapis.com/token']
    token = request.args.get('token', '')
    user_info = verify_google_token(token)
    if user_info is not None:
        user_id, email = user_info
        return f"User ID: {user_id}\nEmail: {email}"
    else:
        return "Invalid token."

def verify_google_token(token):
    try:
        # Specify the Google API endpoint for verifying tokens:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        # Check that the token is valid and is for the correct audience:
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        # Return the user ID and email:
        return (idinfo['sub'], idinfo['email'])
    except ValueError:
        # Invalid token
        return None

if __name__ == '__main__':
    app.run(debug=True)