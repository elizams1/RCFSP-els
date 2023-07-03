# Importing Flask
from flask import Flask, jsonify, render_template

# Creating an instance of the Flask class
app = Flask(__name__)

# Creating a new endpoint with this instance as a function decorator


@app.route('/')
def hello_world():
    return render_template('first-page.html')

# Starting the Server
if __name__ == '__main__':
    app.run()
