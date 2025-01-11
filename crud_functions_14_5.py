import sqlite3

connection = sqlite3.connect("products.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY ,
        title TEXT NOT NULL,
        description TEXT,
        price INT NOT NULL
        );
      ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,          
        username TEXT NOT NULL,          
        email TEXT NOT NULL,             
        age INTEGER NOT NULL,           
        balance INTEGER NOT NULL         
        );
      ''')


def insert_products():
    cursor.execute('DELETE FROM Products')
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (f"Продукт {i}", f"Описание {i}", f"{i*100}"))
    connection.commit()
    connection.close()

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return products

def add_user(username, email, age, balance=1000):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
        (username, email, age, balance))
    connection.commit()


def is_included(username):
    return True \
        if cursor.execute('SELECT COUNT(*) from Users WHERE username = ?',
                          (username, )).fetchone()[0] \
        else False


def products_is_empty():
    return not cursor.execute('SELECT COUNT(*) from Products').fetchone()[0]


if __name__ == '__main__':
    initiate_db()
    if products_is_empty():
        insert_products()
    connection.close()

