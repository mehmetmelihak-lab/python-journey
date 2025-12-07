from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Melih's Flask App!"
