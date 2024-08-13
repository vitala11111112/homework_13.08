import sqlite3
from random import*

con = sqlite3.connect("database.db")
cur = con.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS  NUMBERS(PARITY,NUM STR,INT)""")

cur.execute("""INSERT INTO   NUMBERS(PARITY,NUM)   values('четность', 'число')""")
for i in range(100):
    num = randint(-100,100)
    parity = ""
    if num % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"
    cur.execute('INSERT INTO NUMBERS (parity, num) VALUES (?, ?)', (parity, num))


cur.execute("""SELECT * FROM NUMBERS""")

NUMS = cur.fetchall()
for i in NUMS:
    print(i)
con.close()

