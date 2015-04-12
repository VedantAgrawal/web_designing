from flask import Flask
app=Flask(__name__)
wsgi_app=app.wsgi_app
#Launching server
from new_routing import*
#from routes import *
if __name__=='__main__':
    import os
    HOST=os.environ.get('SERVER_HOAT','localhost')
    try:
        PORT=int(os.environ.get('SERVER_PORT','5555'))
    except ValueError:
        Port=5555
use_reloader=True
app.run()
