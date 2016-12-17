import logging

from flask import Flask
#from google.cloud import pubsub

#client = pubsub.Client()

app = Flask(__name__)


@app.route('/')
def hello():
 #   pulled = subscription.pull(max_messages=2)
    return 'GHS'

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
