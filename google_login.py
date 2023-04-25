# import os
# os.system("start \"\" https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?response_type=code&client_id=1035421752277-7vme3emqji5423fv1s09b64nvam2pfi3.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile&service=lso&o2v=1&flowName=GeneralOAuthFlow")

# import webbrowser
# import subprocess

# webbrowser.open('https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=1035421752277-7vme3emqji5423fv1s09b64nvam2pfi3.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile')

#if(webbrowser.open('https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=1035421752277-7vme3emqji5423fv1s09b64nvam2pfi3.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile')):
# subprocess.Popen(["python", "SignIn.py"])

import subprocess
import webbrowser
import http.server
import socketserver
import urllib.parse

# Define the port number to use for the local web server
PORT = 8000

# Open the Google OAuth 2.0 authorization URL
webbrowser.open('https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=1035421752277-7vme3emqji5423fv1s09b64nvam2pfi3.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost:8000&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile')

# Set up a local web server to listen for the authorization code
class AuthorizationHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        if 'code' in params:
            # Authorization code received - store it and close the web server
            code = params['code'][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Authorization code received - you can now close this browser tab')
            self.server.code = code
        else:
            # Authorization code not received yet - display a waiting message
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Waiting for authorization code...')

httpd = socketserver.TCPServer(("", PORT), AuthorizationHandler)
print(f"Serving on http://127.0.0.1:{PORT}")

# Wait for the user to complete the OAuth authorization process
httpd.handle_request()

# Once the authorization process is complete, get the authorization code and run your desired Python program as a subprocess
code = httpd.code
httpd.server_close()
command = ['python', 'chess_gui.py']  # Replace with the actual path to your Python program
process = subprocess.Popen(command)
process.wait()
print(f"Subprocess returned {process.returncode}")
