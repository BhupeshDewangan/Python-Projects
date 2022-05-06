import sqlite3

def connect():
     conn = sqlite3.connect('routines.db')
     cur = conn.cursor()
     cur.execute("Create Table IF NOT EXISTS routines (Id INTEGER PRIMARY KEY, date text, earnings interger, exercise text, study text, diet text, python text)")
     conn.commit()
     conn.close()

def insert(date, earnings, exercise, study, diet, python):
     conn = sqlite3.connect('routines.db')
     cur = conn.cursor()
     cur.execute("INSERT INTO routines VALUES (NULL, ?, ?, ?, ?, ?, ?)", (date, earnings, exercise, study, diet, python))
     conn.commit()
     conn.close()

def view():
     conn = sqlite3.connect('routines.db')
     cur = conn.cursor()
     cur.execute("SELECT * FROM routines")
     rows = cur.fetchall()
     conn.commit()
     conn.close()
     return  rows

def delete(id):
     conn = sqlite3.connect('routines.db')
     cur = conn.cursor()
     cur.execute("DELETE FROM routines WHERE id= ?", (id,))
     conn.commit()
     conn.close()


def search(date = '', earnings = '', exercise = '', study = '', diet = '', python = ''):
     conn = sqlite3.connect('routines.db')
     cur = conn.cursor()
     cur.execute("SELECT * FROM routines WHERE date = ? OR earnings = ? OR exercise = ? OR study = ? OR diet = ? OR python = ?" , (date, earnings, exercise, study, diet, python))
     rows = cur.fetchall()
     conn.commit()
     conn.close()
     return rows


# ---------------Trying some functions --------------!

# x = search(earnings=500)
# print(x)
# print(view())
# delete(2)
# connect()
# insert('1-2-2022', 200, 'yes exercise', 'yep study hard', 'todays meal is egg', 'go! python')
# insert('1-2-2022', 200, 'yes exercise', 'yep study hard', 'todays meal is egg', 'go! python')
# insert('10-2-2022', 500, 'yes exercise', 'yep study hard', 'todays meal is milk', 'go! python u r awesome')