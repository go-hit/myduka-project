from flask import Flask,render_template,request,redirect,url_for,flash,session
from database import fetch_data,insert_products,insert_sales,insert_stock,product_profit,product_sale,profit_perday,sale_perday,register,check_email
from flask_bcrypt import Bcrypt

app=Flask(__name__)

app.secret_key='gody'

bcrypt=Bcrypt(app)

# home route
@app.route('/')
def home():
    return render_template('index.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    profits=product_profit()
    sale=product_sale()
    product_names=[]
    product_profits=[]
    product_quantity=[]
    for i in profits:
        product_names.append(i[0])
        product_profits.append(float(i[1]))
    for i in sale:
        product_quantity.append(float(i[1]))

    psales=sale_perday()
    # print(psales)
    dates=[]
    dsales=[]
    for i in psales:
        dates.append(str(i[0]))
        dsales.append(float(i[1]))

    pperday=profit_perday()
    datez=[]
    profits=[]
    for i in pperday:
        datez.append(str(i[0]))
        profits.append(float(i[1]))
    return render_template('dashboard.html',productnames=product_names,productprofits=product_profits,
    productquantity=product_quantity,dates=dates,dsales=dsales,datez=datez,profits=profits)

    

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
        flash('product added','success')
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
        flash('sale added','success')
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
        flash('stock added','success')
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

# login route
@app.route('/login', methods=['GET', 'POST'])
def log():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']

        check=check_email(email)
        if check==None:
            flash('Account not found!','danger')
            return redirect(url_for('reg'))
        else:
            if bcrypt.check_password_hash(check[3],password):
            # if password==check[3]:
                session['email']=email
                flash('logged in successfully','success')
                return redirect(url_for('dashboard'))
            else:
                flash('incorrect password or email','danger')
                return redirect(url_for('log'))
    return render_template('login.html')

# Register route
@app.route('/register',methods=['GET','POST'])
def reg():
    if request.method=='POST':
        fname=request.form['name']
        email=request.form['email']
        password=request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user=(fname,email,hashed_password)

        check=check_email(email)
        if check==None:
            register(new_user)
            flash('Account Created successfully','success')
            return redirect(url_for('log'))
        else:
            flash('Already exist, use a different one','danger')
            return redirect(url_for('reg'))    
    return render_template('register.html')


app.run(debug=True)