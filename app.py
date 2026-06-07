from flask import Flask
import requests
import sqlalchemy

app = Flask(__name__)

@app.route("/")
def index():
    return "fake-python-app"

if __name__ == "__main__":
    app.run()
