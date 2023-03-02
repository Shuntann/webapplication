import sqlite3

DATABASE = "database.db"

def create_NewMenu():
    connection = sqlite3.connect(DATABASE)
    connection.execute('CREATE TABLE IF NOT EXIST menus(name, price, description)')
    connection.close()
    