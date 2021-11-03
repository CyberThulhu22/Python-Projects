import sqlite3

database = r"C:\Users\CyberThulhu22\Desktop\QtPySql\Quiz_Py.db"

conn = sqlite3.connect(database)

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_sequence")

data = cursor.fetchall()

number = 0

while number < len(data):
    print(data[number])
    number += 1


print('SELECT * FROM', data[0], 'RANDOM ORDER')


choice_num = input('Choose 1, 2, or 3: ')
choice_num = int(choice_num) - 1

choice = data[choice_num]


print('SELECT * FROM', choice, 'RANDOM ORDER')
