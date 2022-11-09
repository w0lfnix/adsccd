from flask import *

app = Flask(__name__)

@app.route("/a", methods=['POST'])
def a():
    return request.get_json()['a']


app.run()
