from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    name = request.args.get("name")
    return f"<p>Hello friend {escape(name)}</p>"
