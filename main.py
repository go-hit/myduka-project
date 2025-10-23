from flask import Flask,render_template

app=Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('index.html')

# products route
@app.route('/products')
def products():
    return render_template('products.html')

# sales route
@app.route('/sales')
def sales():
    return render_template('sales.html')

# stock route
@app.route('/stock')
def stock():
    return render_template('stock.html')

app.run()