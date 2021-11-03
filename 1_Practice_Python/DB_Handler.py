import sqlite3
from sqlite3 import Error

def sql_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
        print("Connected")
    except Error as e:
        print(e)

    return None

def show_all_db(conn):
    c = conn.cursor()
    c.execute('SELECT * FROM QuizTest')
    data = c.fetchall()
    for row in data:
        print(row)

def update_db(conn):
    c = conn.cursor()
    c.execute('UPDATE QuizTest set Answer = asdf where ID = *')
    conn.commit
    print "Total number of rows update :", conn.total_changes

def main():
    database = "/Users/theenawman/Documents/GitHub/WiredUpQuiz/Test_JGN/main.db"
    conn = sql_connection(database)
    with conn:
        print("Printing all table data")
        show_all_db(conn)

def menu():
    print (30 * '-')
    print ("   M A I N - M E N U")
    print (30 * '-')
    print ("1. Show All DB Entrys")
    print ("2. Delete Entry")
    print ("3. Update Entry")
    print ("4. Exit")
    print (30 * '-')

    selection=raw_input("Please Select A Choice:")
    selection=int(selection)
    if selection == 1:
        main()
    elif selection == 2:
        print("b")
    elif selection == 3:
        print("c")
    elif selection == 4:
        print("Exit")
    else:
        print("Unknown Command")


if __name__ == '__main__':
    menu()
