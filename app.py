# Importing Flask
from flask import Flask, jsonify

# Creating an instance of the Flask class
app = Flask(__name__)

# Creating a new endpoint with this instance as a function decorator


@app.route('/')
def hello_world():
    return "HELLO THIS APP"

# Starting the Server
if __name__ == '__main__':
    app.run()
