names = ["Himanshu", "Rahul", "Priya", "Amit"]

while True:
    print("\nMenu:")
    print("1. Show all names")
    print("2. Add name")
    print("3. Remove name")
    print("4. Search name")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Names:", names)

    elif choice == "2":
        new_name = input("Enter name to add: ").strip().title()
        if new_name in names:
            print("Name already exists.")
        else:
            names.append(new_name)
            print("Name added successfully.")

    elif choice == "3":
        remove_name = input("Enter name to remove: ").strip().title()
        if remove_name in names:
            names.remove(remove_name)
            print("Name removed successfully.")
        else:
            print("Name not found.")

    elif choice == "4":
        search_name = input("Enter name to search: ").strip().title()
        if search_name in names:
            print("Name found.")
        else:
            print("Name not found.")

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
