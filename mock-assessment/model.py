#!usr/bin/env python3

import sqlite3

def add_user(username,password):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute(
        '''INSERT INTO account(
            username,
            password
        )VALUES(?,?);''',
        (username,password)
    )
    connection.commit()
    connection.close()

def insert_account_details(uname, fname, lname, dob, phone_num, address):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()

    cursor.execute('''UPDATE account SET fname="{}", lname="{}", dob="{}", phone_num="{}", address="{}"
        WHERE username = "{}";'''.format(fname,lname,dob,phone_num,address,uname))

    connection.commit()
    connection.close()

class Login:
    def __init__(self,objectified_username, objectified_password):
        self.objectified_username = objectified_username
        self.objectified_password = objectified_password

    def lookup_username(uname):
        connection = sqlite3.connect('info.db')
        cursor = connection.cursor()
        objectified_username = cursor.execute(
        '''SELECT username FROM account WHERE username="{}";'''.format(uname))
        data = cursor.fetchall()

        connection.commit()
        connection.close()
        return data[0][0]

    def lookup_password(uname):
        print(uname)
        connection = sqlite3.connect('info.db')
        cursor = connection.cursor()
        objectified_password = cursor.execute(
        '''SELECT password FROM account WHERE username="{}";'''.format(uname))        
        data = cursor.fetchall()

        connection.commit()
        connection.close()
        return data[0][0]


def read_fname_by_last_name(something):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute('SELECT fname FROM account WHERE lname="{}"'.format(something))
    z = cursor.fetchall()[0][0]
    print(z)

def read_lname_by_first_name(something):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute('SELECT lname FROM account WHERE fname="{}"'.format(something))
    z = cursor.fetchall()[0][0]
    print(z)

def read_dob_by_first_name(something):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute('SELECT dob FROM account WHERE fname="{}"'.format(something))
    z = cursor.fetchall()[0][0]
    print(z)

def read_ph_num_by_first_name(something):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute('SELECT phone_num FROM account WHERE fname="{}"'.format(something))
    z = cursor.fetchall()[0][0]
    print(z)

def read_address_by_first_name(something):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute('SELECT address FROM account WHERE fname="{}"'.format(something))
    z = cursor.fetchall()[0][0]
    print(z)


if __name__ == '__main__':
    read_fname_by_last_name('Modi')
    read_lname_by_first_name('Narendra')
    read_dob_by_first_name('Narendra')
    read_ph_num_by_first_name('Narendra')
    read_address_by_first_name('Narendra')
