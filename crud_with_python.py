import json

items_file = "items_list.text"

def show_all_items(items):
    #added enumerate to add indexing
    for index, item in enumerate(items, start=1): 
        print(f"{index}.{item['name']} , Time to finish: {item['alloted_time']}")

def add_item(items):
    name = input("Enter the Item name : ")
    alloted_time = input("Time to complete : ")
    items.append({"name": name, "alloted_time": alloted_time})

    save_data(items)

def update_item(items):
    show_all_items(items)   
    update_item_idx = int(input("Enter the item number you want to update : "))
    if(1 <= update_item_idx <= len(items)):
        name = input("Enter the Item name : ")
        alloted_time = input("Time to complete : ")
        items[update_item_idx - 1] = {"name": name, "alloted_time": alloted_time}        
        save_data(items)
    else:
        print("Invalid index selected")

def remove_item(items):
    show_all_items(items)
    delete_item_idx = int(input("Enter the item number you want to delete : "))

    if(1 <= delete_item_idx <= len(items)):        
        del items[delete_item_idx - 1]
        save_data(items)
    else:
        print("Invalid index selected")

def load_data():
    try:
        with open(items_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(items):
    with open(items_file, 'w') as file:
        return json.dump(items, file)

def main():
    items = load_data()
    while True:
        print("\n Please select one option")
        print("Please choose 1 to show all items in your list")
        print("Please choose 2 to add an item in your list")
        print("Please choose 3 to update an item in your list")
        print("Please choose 4 to delete an item from your list")
        print("Please choose 5 to exit the app")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                show_all_items(items)
            case "2":
                add_item(items)
            case "3":
                update_item(items)
            case "4":
                remove_item(items)
            case "5":
                break
            case _:
               print("Invalid input")

if __name__ == "__main__":
    main()


     
