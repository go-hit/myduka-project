from flask import Flask,render_template
from database import fetch_data


app=Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('index.html')

# products route
@app.route('/products')
def products():
    prods=fetch_data('products')
    return render_template('products.html',myprods=prods)

# sales route
@app.route('/sales')
def sales():
    sal=fetch_data('sales')
    return render_template('sales.html',mysal=sal)

# stock route
@app.route('/stock')
def stock():
    stoc=fetch_data('stock')
    return render_template('stock.html',mystoc=stoc)

app.run()