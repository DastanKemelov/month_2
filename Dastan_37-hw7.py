import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL DEFAULT 0.0 NOT NULL,
        quantity INTEGER DEFAULT 0 NOT NULL
    )
''')

def add_products():
    products = [
        ('Товар 1', 10.99, 50),
        ('Товар 2', 25.5, 30),
        ('Товар 3', 5.0, 100),

    ]
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()

def update_quantity(product_id, new_quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()

def update_price(product_id, new_price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()

# Вывод всех товаров из БД
def print_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)

def print_products_below_limit():
    limit_price = 100
    limit_quantity = 5
    cursor.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (limit_price, limit_quantity))
    products = cursor.fetchall()
    for product in products:
        print(product)


def search_products_by_title(title):
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + title + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)

search_products_by_title('мыло')


add_products()
print_all_products()
update_quantity(1, 60)
update_price(2, 30.0)
delete_product(3)
print_products_below_limit()
search_products_by_title('Товар')

conn.close()
