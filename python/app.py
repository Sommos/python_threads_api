from threads_api.src.threads_api import ThreadsAPI
from flask import Flask, jsonify

import main

app = Flask(__name__)

# saves instance of ThreadsAPI class to variable api
api = ThreadsAPI()

@app.route('/data')
def data():
    # call main.py functions
    user_id = main.get_user_id(api, "zuck")
    profile = main.get_user_profile(api, "zuck", user_id)
    threads = main.get_user_threads(api, "zuck", user_id, 10)
    replies = main.get_user_replies(api, "zuck", user_id, 10)
    # return the data as JSON 
    return jsonify({
        'profile': profile,
        'threads': threads,
        'replies': replies
    })

if __name__ == '__main__':
    app.run()