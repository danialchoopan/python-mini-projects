import sqlite3
import os

#create database
db_connection=sqlite3.connect('phonebook.sqlite')

#create tables
db_connection.execute("""
CREATE TABLE IF NOT EXISTS phonebook(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
    name TEXT,
    phone TEXT
) 
""")

while True:
    #clear terminal
    os.system('cls')

    #print menu
    print("phonebook 1 ")
    print("1-show")
    print("2-add")
    print("3-update")
    print("4-delete")
    print("0-exit")
    #select item
    user_input=int(input(': '))

    #show phones
    if user_input==1:
        print("name phone book")
        db_cursor=db_connection.cursor()
        for phone in db_cursor.execute("SELECT* FROM phonebook"):
            print("id: {phone_id} | name: {phone_name} | phone: {phone_phone})".format(
                phone_id=phone[0],
                phone_name=phone[1],
                phone_phone=phone[2]
            ))
        input("enter any key to continue ")
    
    #add phone
    elif user_input==2:
        print("add new phone")
        name=input("enter name: ")
        phone=input("enter phone: ")
        db_cursor=db_connection.cursor()
        db_cursor.execute("INSERT INTO phonebook(name,phone) VALUES(?,?)",(name,phone))
        db_connection.commit()
        print("done")
        input("enter any key to continue ")

    #update phone
    elif user_input==3:
        print("update phone")
        id=input("enter phone id: ")
        name=input("enter name: ")
        phone=input("enter phone: ")
        db_cursor=db_connection.cursor()
        db_cursor.execute("UPDATE phonebook SET name=?, phone=? WHERE id=?",(name,phone,id))
        db_connection.commit()
        print("done")
        input("enter any key to continue ")

    #delete phone
    elif user_input==4:
        print("delete phone")
        id=input("enter phone id: ")
        db_cursor=db_connection.cursor()
        db_cursor.execute("DELETE FROM phonebook WHERE id=?",(id))
        db_connection.commit()
        print("done")
        input("enter any key to continue ")

    
    
    #exit
    elif user_input==0:
        break

    #error
    else:
        print("error")
        break