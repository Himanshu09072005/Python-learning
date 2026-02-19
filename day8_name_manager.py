def load_names():
    try:
        with open("names.txt", "r") as file:
            return [n.strip() for n in file.readlines()]
    except FileNotFoundError:
        return []


def save_name(name):
    with open("names.txt", "a") as file:
        file.write(name + "\n")


def show_names():
    names = load_names()
    if names:
        print("Names:", names)
    else:
        print("No names found.")


def add_name():
    name = input("Enter name to add: ").strip().title()
    names = load_names()
    
    if name in names:
        print("Name already exists.")
    else:
        save_name(name)
        print("Name added successfully.")


def search_name():
    name = input("Enter name to search: ").strip().title()
    names = load_names()
    
    if name in names:
        print("Name found.")
    else:
        print("Name not found.")


def main():
    while True:
        print("\nMenu:")
        print("1. Show names")
        print("2. Add name")
        print("3. Search name")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            show_names()
        elif choice == "2":
            add_name()
        elif choice == "3":
            search_name()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


main()
