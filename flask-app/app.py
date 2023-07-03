# Importing Flask
from flask import Flask, jsonify, render_template

# Creating an instance of the Flask class
app = Flask(__name__)

# Creating a new endpoint with this instance as a function decorator
df_product = pd.read_csv(
    '/static/data/DataProdukVers5.csv')

df_html = df_product.values

@app.route('/')
def hello_world():
    return render_template('first-page.html')

@app.route('/second')
def sec_page():
    return render_template('second-page.html', data=df_html)

# Starting the Server
if __name__ == '__main__':
    app.run()
