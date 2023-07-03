# Importing Flask
from flask import Flask, jsonify, render_template, request, url_for
import pandas as pd
# Creating an instance of the Flask class
app = Flask(__name__, static_url_path='', static_folder="./static")

# Creating a new endpoint with this instance as a function decorator

df_product = pd.read_csv('/flask-app/static/data/DataProdukVers5.csv')

df_html = df_product.values

@app.route('/', methods=['GET','POST'])
def hello_world():
    return render_template('first-page.html')


@app.route('/second', methods=['GET', 'POST'])
def sec_page():
    
    if request.method == 'GET':
        return render_template('second-page.html', data=df_html)


# Starting the Server
if __name__ == '__main__':
    app.run(debug=True)
