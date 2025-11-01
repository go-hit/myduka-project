from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_products,insert_sales,insert_stock,product_profit


app=Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('index.html')

# Dasshboard route
@app.route('/dashboard')
def dashboard():
    profits=product_profit()
    product_names=[]
    product_profits=[]
    for i in profits:
        product_names.append(i[0])
        product_profits.append(float(i[1]))
    return render_template('dashboard.html',productnames=product_names,productprofits=product_profits)



# create a python function that receives data from frontend to serverside/flask
@app.route('/add_products',methods=['GET','POST'])
def add_products():
    # checking method
    if request.method=='POST':
        pname=request.form['name']
        bp=request.form['buying_price']
        sp=request.form['selling_price']
        new_product=(pname,bp,sp)
        # insert to database
        insert_products(new_product)
    return redirect(url_for('products'))# the url is from the function in /products(route) not route(/add_products)

@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    # checking method
    if request.method=='POST':
        pid=request.form['pid']
        quantity=request.form['quantity']
        new_sale=(pid,quantity)
        # insert to database
        insert_sales(new_sale)
    return redirect(url_for('sales'))

@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    # checking method
    if request.method=='POST':
        pid=request.form['pid']
        s_quantity=request.form['stock_quantity']
        new_stock=(pid,s_quantity)
        # insert to database
        insert_stock(new_stock)
    return redirect(url_for('stock'))




# products route
@app.route('/products')
def products():
    prods=fetch_data('products')
    return render_template('products.html',myprods=prods)

# sales route
@app.route('/sales')
def sales():
    sal=fetch_data('sales')
    prodz=fetch_data('products')
    return render_template('sales.html',mysal=sal,myprodz=prodz)

# stock route
@app.route('/stock')
def stock():
    stoc=fetch_data('stock')
    prodz=fetch_data('products')
    return render_template('stock.html',mystoc=stoc,myprodz=prodz)

app.run(debug=True)