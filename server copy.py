from flask import Flask
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return 'HELLO WORLD f'
