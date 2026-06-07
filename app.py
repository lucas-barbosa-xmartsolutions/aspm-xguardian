from flask import Flask
import requests
import yaml

app = Flask(__name__)

@app.route("/")
def index():
    return "fake-python-app"

if __name__ == "__main__":
    app.run()
