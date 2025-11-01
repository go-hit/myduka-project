import psycopg2
#connect to postgres database by declaring a variable
conn=psycopg2.connect(
    host='localhost',
    user='postgres',
    port=5432,
    dbname='myduka_db',
    password='gody'
)
#declare cursor to perfom database operations
curr=conn.cursor()

#fetch products
# curr.execute('select * from products;')
# products=curr.fetchall()
# print(products)

#fetch sales
# curr.execute('select * from sales;')
# sales=curr.fetchall()
# print(sales)

#fetch stock 
# curr.execute('select * from stock;')
# stock=curr.fetchall()
# print(stock)

# def fetch_products():
#     curr.execute('select * from products;')
#     products=curr.fetchall()
#     return products
# prods=fetch_products()
# print('my products')
# print(prods)

# def fetch_sales():
#     curr.execute('select * from sales;')
#     sales=curr.fetchall()
#     return sales
# sal=fetch_sales()
# print('my sales')
# print(sal)

# def fetch_stock():
#     curr.execute('select * from stock;')
#     stock=curr.fetchall()
#     return stock
# stoc=fetch_stock()
# print('my stock')
# print(stoc)

# inserting sales data
# curr.execute('insert into sales(pid,quantity,created_at)values(1,10,now()),(2,15,now()),(3,40,now()),(4,23,now()),(5,35,now());')
# conn.commit()

# inserting stock data
# curr.execute('insert into stock(pid,stock_quantity)values(1,120),(2,115),(3,240),(4,323),(5,235);')
# conn.commit()


def fetch_data(table_name):
    curr.execute(f'select * from {table_name}')
    data=curr.fetchall()
    return data
# products=fetch_data('products')
# print(products)


# adding a data one by one without repeating the full query
def insert_products(values):
    query='insert into products(name,buying_price,selling_price)values(%s,%s,%s);'
    curr.execute(query,values)
    conn.commit()
# new_product=('salt',50,70)
# insert_products(new_product) 

def insert_sales(values):
    query='insert into sales(pid,quantity,created_at)values(%s,%s,now());'
    curr.execute(query,values)
    conn.commit()
# new_sales=(6,50)
# insert_sales(new_sales)    


def insert_stock(values):
    query='insert into stock(pid,stock_quantity)values(%s,%s);'
    curr.execute(query,values)
    conn.commit()


# function to get profit per product
def product_profit():
    query='select p.name,sum((p.selling_price-p.buying_price)*s.quantity) as profits from products as p join sales as s on p.id=s.pid group by p.name;'
    curr.execute(query)
    profit=curr.fetchall()
    return profit
# my_profit=product_profit()
# print('Profits')
# print(my_profit)

# function to get sales per product
def product_sale():
    query='select p.name,p.id,sum(selling_price*quantity) as total_sales from products as p join sales as s on p.id=s.pid group by p.name,p.id;'
    curr.execute(query)
    sales=curr.fetchall()
    return sales
# sales=product_sale()
# print('Sales made')
# print(sales)