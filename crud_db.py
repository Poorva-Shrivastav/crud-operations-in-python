import sqlite3

conn = sqlite3.connect("list_items.db")

#to execute SQL statements and fetch results from SQL queries, we use cursor.
cursor = conn.cursor() 

cursor.execute('''
    CREATE TABLE IF NOT EXISTS list_items (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               alloted_time TEXT NOT NULL
    )
''')

def display_list():
    res = cursor.execute("SELECT * FROM list_items")
    # returns a tuple with all the data from the query. We can chose to opt for fetchall  or fetchone    
    for row in cursor.fetchall():
        print(row)
 

def add_item(name, alloted_time):
    cursor.execute("INSERT INTO list_items(name, alloted_time) VALUES(?, ?)", (name, alloted_time))    
    conn.commit()

def update_item(idx, new_name, alloted_time):
    cursor.execute("UPDATE list_items SET name = ?, alloted_time = ? WHERE id = ?", (new_name, alloted_time, idx))
    conn.commit()


def delete_item(idx):
    cursor.execute("DELETE from list_items WHERE id = ? ", (idx, )) #whenever we insert a single value, we need to insert it with a comma and it's not a tupple.
    conn.commit()
 
def main():
    while True: 
        print("\n Please select one option")
        print("Please choose 1 to show all items in your list")
        print("Please choose 2 to add an item in your list")
        print("Please choose 3 to update an item in your list")
        print("Please choose 4 to delete an item from your list")
        print("Please choose 5 to exit the app")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("1")
            display_list()

        elif choice == "2":
            name = input("Enter the Item name : ")
            alloted_time = input("Time to complete : ")
            add_item(name, alloted_time)
        
        elif choice=="3":
            idx = int(input("Enter the Item id to update : "))
            new_name = input("Enter the new Item name : ")
            alloted_time = input("Time to complete : ")
            update_item(idx, new_name, alloted_time)
        
        elif choice=="4":
            idx = int(input("Enter the Item id to delete : "))          
            delete_item(idx)

        elif choice == "5":
            break

        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()

