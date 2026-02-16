FILENAME = "names.txt"

def load_names():
    try:
        with open(FILENAME, "r") as file:
            names = file.read().splitlines()
    except FileNotFoundError:
        names = []
    return names


def save_names(names):
    with open(FILENAME, "w") as file:
        for name in names:
            file.write(name + "\n")

names = load_names()

while True:
    print("\nMenu:")
    print("1. Show all names")
    print("2. Add name")
    print("3. Remove name")
    print("4. Search name")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(names) == 0:
            print("No names found.")
        else:
            print("Names:", names)

    elif choice == "2":
        new_name = input("Enter name to add: ")
        names.append(new_name)
        save_names(names)
        print("Name added successfully.")

    elif choice == "3":
        rem_name = input("Enter name to remove: ")
        if rem_name in names:
            names.remove(rem_name)
            save_names(names)
            print("Name removed successfully.")
        else:
            print("Name not found.")

    elif choice == "4":
        search_name = input("Enter name to search: ")
        if search_name in names:
            print("Name found.")
        else:
            print("Name not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
