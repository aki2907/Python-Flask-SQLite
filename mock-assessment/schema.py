#!usr/bin/env python3

import sqlite3

connection = sqlite3.connect('info.db')
cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE account(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(64),
        password VARCHAR(64),
        fname VARCHAR(64),
        lname VARCHAR(64),
        dob VARCHAR(64),
        phone_num VARCHAR(64),
        address VARCHAR(128)
    );'''
)

cursor.execute(
    '''INSERT INTO account(
        username,
        password,
        fname,
        lname,
        dob,
        phone_num,
        address
        ) VALUES(
        "narmodi",
        "india",
        "Narendra",
        "Modi",
        "01-01-1955",
        "123-456-7890",
        "321, PM House, New Delhi, India 110001"
    );'''
)

connection.commit()
cursor.close()
connection.close()
